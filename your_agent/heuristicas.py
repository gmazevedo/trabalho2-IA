import sys
sys.path.append('./your_agent')
from auxiliares import *
from dados import *

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
