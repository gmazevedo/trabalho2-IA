import sys
from your_agent.auxiliares import *
from your_agent.dados import *

LINHA = 0
COLUNA = 1

#Pontos:
# * Cada posição do tabuleiro tem um valor, ver no arquivo dados.py
def heuristica_pecas_posicao(the_board, color, enemy_color):
    pontos = 0

    for l in range(0, 7):
        for c in range(0, 7):

            if the_board.tiles[l][c] == color:
                pontos += valor_tabuleiro[l][c]

            elif the_board.tiles[l][c] == enemy_color:
                pontos -= valor_tabuleiro[l][c]

    return pontos

#Pontos = diferença dos meus movimentos para o do adversário
#Positivo se eu tiver mais, negativo se ele tiver mais
def heuristica_comparacao_movimentos(the_board, color, enemy_color):
    proximos_movimentos_inimigo = the_board.legal_moves(enemy_color)
    pontos_movimento_inimigo = len(proximos_movimentos_inimigo)

    proximos_movimentos = the_board.legal_moves(color)
    pontos_movimento = len(proximos_movimentos)

    pontos = pontos_movimento - pontos_movimento_inimigo

    return pontos

#Retorna positivo se o adversário não captura, negativo se captira
def heuristica_captura_aliado(the_board, enemy_color, movimento):
    PONTUACAO = 3
    proximos_movimentos_inimigo = the_board.legal_moves(enemy_color)
    pontos = PONTUACAO
    for movimento_inimigo in proximos_movimentos_inimigo:
        if(movimento_inimigo[0] == movimento[0] and movimento_inimigo[1] == movimento[1]):
            pontos *= -1
            break

    return pontos

#Retorna a quantidade de pecas capturadas
def heuristica_qtde_pecas_capturadas(the_board, color, movimento):
    qtde_de_pecas_antes = the_board.piece_count[color]

    the_board.process_move(movimento, color)

    return the_board.piece_count[color] - qtde_de_pecas_antes

def heuristica_qtde_pecas_final(the_board, color, enemy_color):
    qtde_de_pecas_color = the_board.piece_count[color]
    qtde_de_pecas_enemy_color = the_board.piece_count[enemy_color]

    if(qtde_de_pecas_color < qtde_de_pecas_enemy_color):
        return -10000
    else:
        return 10000

#Retorna 1000 se a posição é estável, 0 se não for.
#Objetivo é fazer com que se jogue na maior quantidade
#de posições estáveis possíveis
def heuristica_posicao_estavel(movimento, posicoes_estaveis_posicao):
    l_movimento = movimento[LINHA]
    c_movimento = movimento[COLUNA]

    #Posicao não é estável?
    if not posicoes_estaveis_posicao[l_movimento][c_movimento]:
        return 0

    #É estável:
    esq = c_movimento-1
    dir = c_movimento+1
    cima = l_movimento-1
    baixo = l_movimento-1

    #Linha de canto?
    if movimento[LINHA] == CANTO_1 or movimento[LINHA] == CANTO_2:
        #Esquerda
        if esq >= 0:
            posicoes_estaveis_posicao[l_movimento][esq] = True
        #Direita
        if dir <= 7:
            posicoes_estaveis_posicao[l_movimento][dir] = True
    #Não é linha de canto
    else:
        #Verifíca se a posição da esquerda é estável
        if posicoes_estaveis_posicao[baixo][esq] or posicoes_estaveis_posicao[cima][esq]:
            posicoes_estaveis_posicao[l_movimento][esq] = True
        #Verifíca se a posição da direita é estável
        elif posicoes_estaveis_posicao[baixo][dir] or posicoes_estaveis_posicao[cima][dir]:
            posicoes_estaveis_posicao[l_movimento][dir] = True
    
    #Coluna de canto?
    if movimento[COLUNA] == CANTO_1 or movimento[COLUNA] == CANTO_2:
        #Cima
        if cima >= 0:
            posicoes_estaveis_posicao[cima][c_movimento] = True
        #Baixo
        if baixo <= 7:
            posicoes_estaveis_posicao[baixo][c_movimento] = True
    #Não é coluna de canto
    else:
        #Verifíca se a posição de cima é estável
        if posicoes_estaveis_posicao[cima][esq] or posicoes_estaveis_posicao[cima][dir]:
            posicoes_estaveis_posicao[cima][c_movimento] = True
        #Verifíca se a posição de baixo é estável
        elif posicoes_estaveis_posicao[baixo][esq] or posicoes_estaveis_posicao[baixo][dir]:
            posicoes_estaveis_posicao[cima][c_movimento] = True

    return 1000

#Não está sendo usada
def heuristica_pecas_centros(the_board, color):
    pontos = 0

    #Ve que tem
    for l in range(2, 6):
        for c in range(2, 6):
            if the_board.tiles[l][c] == color:
                pontos += 1
            else:
                pontos -= 1

    return pontos

#Não está sendo usada
def heuristica_peca_cantos(the_board, color):
    pontos = 0

    #Ve se tem
    lista = [(0,0), (7,7), (0,7), (7,0)]
    for i in lista:
        if(the_board.tiles[i[0]][i[1]] == color):
            pontos += 1

    return pontos

