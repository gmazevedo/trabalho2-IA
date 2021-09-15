def is_peca_canto(l, c):
    if((l == 0 and c == 0)
        or (l == 7 and c == 7)
        or (l == 0 and c == 7)
        or (l == 7 and c == 0)):
        return True
    
    return False

def is_peca_meio(l, c):
    if(l >=2 and l <= 5 and c >=2 and c <= 5):
        return True
    
    return False

def jogada_centro(movimento, the_board, color):
    
    meio_livre = False

    for l in range(2, 6):
        for c in range(2, 6):
            if the_board.tiles[l][c] == '.':
                if the_board.is_legal(movimento, color):
                    meio_livre = True
                    break
            
        if meio_livre:
            break


    if meio_livre and not (movimento[0] >= 2 and movimento[0] <= 5 and movimento[1] >= 2 and movimento[1] <= 5):
        return False
    
    return True

def pega_canto(movimento, the_board):

    lista = [(0,0), (7,7), (0,7), (7,0)]
    canto = False
    for i in lista:
        if(the_board.tiles[i[0]][i[1]] == '.'):
            if(movimento[0] == i[0] and movimento[1] == i[1]):
                canto = True
                break

    return canto
    '''
    if(the_board.tiles[0][0] == color
        or the_board.tiles[7][7] == color  
        or the_board.tiles[0][7] == color 
        or the_board.tiles[7][0] == color):
    '''
         
def pula_comparacao(movimento, the_board, color):
    if not jogada_centro(movimento, the_board, color):
        return True 
    
    if pega_canto(movimento, the_board):
        return False
    
    return False

#############
from frank.dados import *

LINHA = 1
COLUNA = 0

def add_posicao_estavel(movimento, posicoes_estaveis_posicao, mudar_valores=False):
    l_movimento = movimento[LINHA]
    c_movimento = movimento[COLUNA]
    #É estável:
    esq = c_movimento-1
    dir = c_movimento+1
    cima = l_movimento-1
    baixo = l_movimento-1

    dir_cima_baixo = dir <= 7 and cima >= 0 and baixo <= 7
    esq_cima_baixo = esq <= 7 and cima >= 0 and baixo <= 7
    esq_cima_dir = esq <= 7 and cima >= 0 and dir <= 7 
    esq_baixo_dir = esq <= 7 and baixo <= 7 and dir <= 7 

    #Linha de canto?
    if movimento[LINHA] == CANTO_1 or movimento[LINHA] == CANTO_2:
        #Esquerda
        if esq >= 0:
            posicoes_estaveis_posicao[l_movimento][esq] = True
            valor_tabuleiro[l_movimento][esq] = POSICAO_ESTAVEL
        #Direita
        if dir <= 7:
            posicoes_estaveis_posicao[l_movimento][dir] = True
            valor_tabuleiro[l_movimento][dir] = POSICAO_ESTAVEL
    #Não é linha de canto
    else:
        #Verifíca se a posição da esquerda é estável
        if esq_cima_baixo:
            if posicoes_estaveis_posicao[baixo][esq] or posicoes_estaveis_posicao[cima][esq]:
                posicoes_estaveis_posicao[l_movimento][esq] = True
                valor_tabuleiro[l_movimento][esq] = POSICAO_ESTAVEL
        #Verifíca se a posição da direita é estável
            elif dir_cima_baixo:
                if posicoes_estaveis_posicao[baixo][dir] or posicoes_estaveis_posicao[cima][dir]:
                    posicoes_estaveis_posicao[l_movimento][dir] = True
                    valor_tabuleiro[l_movimento][dir] = POSICAO_ESTAVEL
    
    #Coluna de canto?
    if movimento[COLUNA] == CANTO_1 or movimento[COLUNA] == CANTO_2:
        #Cima
        if cima >= 0:
            posicoes_estaveis_posicao[cima][c_movimento] = True
            valor_tabuleiro[cima][c_movimento] = POSICAO_ESTAVEL
        #Baixo
        if baixo <= 7:
            posicoes_estaveis_posicao[baixo][c_movimento] = True
            valor_tabuleiro[baixo][c_movimento] = POSICAO_ESTAVEL
    #Não é coluna de canto
    else:
        #Verifíca se a posição de cima é estável
        if esq_cima_dir:
            if posicoes_estaveis_posicao[cima][esq] or posicoes_estaveis_posicao[cima][dir]:
                posicoes_estaveis_posicao[cima][c_movimento] = True
                valor_tabuleiro[cima][c_movimento] = POSICAO_ESTAVEL
        #Verifíca se a posição de baixo é estável
        elif esq_baixo_dir:
            if posicoes_estaveis_posicao[baixo][esq] or posicoes_estaveis_posicao[baixo][dir]:
                posicoes_estaveis_posicao[baixo][c_movimento] = True
                valor_tabuleiro[baixo][c_movimento] = POSICAO_ESTAVEL

def verifica_add_posicao_estavel(movimento, posicoes_estaveis_posicao):
    l_movimento = movimento[LINHA]
    c_movimento = movimento[COLUNA]

    #Posicao não é estável?
    if not posicoes_estaveis_posicao[l_movimento][c_movimento]:
        return False

    add_posicao_estavel(movimento, posicoes_estaveis_posicao)

    return True

#####################

def novo_add_posicao_estavel(movimento, posicoes_estaveis_posicao, the_board, color):
    l_movimento = movimento[LINHA]
    c_movimento = movimento[COLUNA]
    #É estável:
    esq = c_movimento-1
    dir = c_movimento+1
    cima = l_movimento-1
    baixo = l_movimento+1

    dir_cima_baixo = dir <= 7 and cima >= 0 and baixo <= 7
    esq_cima_baixo = esq >= 0 and cima >= 0 and baixo <= 7
    esq_cima_dir = esq >= 0 and cima >= 0 and dir <= 7 
    esq_baixo_dir = esq >= 0 and baixo <= 7 and dir <= 7 

    #Linha de canto?
    if movimento[LINHA] == CANTO_1 or movimento[LINHA] == CANTO_2:
        #Esquerda
        if esq >= 0 and not posicoes_estaveis_posicao[l_movimento][esq]:
            posicoes_estaveis_posicao[l_movimento][esq] = True

            if(the_board.tiles[l_movimento][esq] == color):
                novo_add_posicao_estavel((l_movimento, esq), posicoes_estaveis_posicao, the_board, color)

            valor_tabuleiro[l_movimento][esq] = POSICAO_ESTAVEL
        #Direita
        if dir <= 7 and not posicoes_estaveis_posicao[l_movimento][dir]:
            posicoes_estaveis_posicao[l_movimento][dir] = True

            if(the_board.tiles[l_movimento][dir] == color):
                novo_add_posicao_estavel((l_movimento, dir), posicoes_estaveis_posicao, the_board, color)

            valor_tabuleiro[l_movimento][dir] = POSICAO_ESTAVEL
    #Não é linha de canto
    else:
        #Verifíca se a posição da esquerda é estável
        if esq_cima_baixo:
            if posicoes_estaveis_posicao[baixo][esq] or posicoes_estaveis_posicao[cima][esq]:
                if not posicoes_estaveis_posicao[l_movimento][esq]:
                    posicoes_estaveis_posicao[l_movimento][esq] = True

                    if(the_board.tiles[l_movimento][esq] == color):
                        novo_add_posicao_estavel((l_movimento, esq), posicoes_estaveis_posicao, the_board, color)

                    valor_tabuleiro[l_movimento][esq] = POSICAO_ESTAVEL
        #Verifíca se a posição da direita é estável
            elif dir_cima_baixo:
                if posicoes_estaveis_posicao[baixo][dir] or posicoes_estaveis_posicao[cima][dir]:
                    if not posicoes_estaveis_posicao[l_movimento][dir]:
                        posicoes_estaveis_posicao[l_movimento][dir] = True

                        if(the_board.tiles[l_movimento][dir] == color):
                            novo_add_posicao_estavel((l_movimento, dir), posicoes_estaveis_posicao, the_board, color)

                        valor_tabuleiro[l_movimento][dir] = POSICAO_ESTAVEL
    
    #Coluna de canto?
    if movimento[COLUNA] == CANTO_1 or movimento[COLUNA] == CANTO_2:
        #Cima
        if cima >= 0 and not posicoes_estaveis_posicao[cima][c_movimento]:
            posicoes_estaveis_posicao[cima][c_movimento] = True

            if(the_board.tiles[cima][c_movimento] == color):
                novo_add_posicao_estavel((cima, c_movimento), posicoes_estaveis_posicao, the_board, color)

            valor_tabuleiro[cima][c_movimento] = POSICAO_ESTAVEL
        #Baixo
        if baixo <= 7 and not posicoes_estaveis_posicao[baixo][c_movimento]:
            posicoes_estaveis_posicao[baixo][c_movimento] = True

            if(the_board.tiles[baixo][c_movimento] == color):
                novo_add_posicao_estavel((baixo, c_movimento), posicoes_estaveis_posicao, the_board, color)

            valor_tabuleiro[baixo][c_movimento] = POSICAO_ESTAVEL
    #Não é coluna de canto
    else:
        #Verifíca se a posição de cima é estável
        if esq_cima_dir:
            if posicoes_estaveis_posicao[cima][esq] or posicoes_estaveis_posicao[cima][dir]:
                if not posicoes_estaveis_posicao[cima][c_movimento]:
                    posicoes_estaveis_posicao[cima][c_movimento] = True

                    if(the_board.tiles[cima][c_movimento] == color):
                        novo_add_posicao_estavel((cima, c_movimento), posicoes_estaveis_posicao, the_board, color)

                    valor_tabuleiro[cima][c_movimento] = POSICAO_ESTAVEL
        #Verifíca se a posição de baixo é estável
        elif esq_baixo_dir:
            if posicoes_estaveis_posicao[baixo][esq] or posicoes_estaveis_posicao[baixo][dir]:
                if not posicoes_estaveis_posicao[baixo][c_movimento]:
                    posicoes_estaveis_posicao[baixo][c_movimento] = True

                    if(the_board.tiles[cima][c_movimento] == color):
                        novo_add_posicao_estavel((cima, c_movimento), posicoes_estaveis_posicao, the_board, color)

                    valor_tabuleiro[baixo][c_movimento] = POSICAO_ESTAVEL

def novo_verifica_add_posicao_estavel(movimento, posicoes_estaveis_posicao, the_board, color):
    if movimento is None:
        return False
    
    l_movimento = movimento[LINHA]
    c_movimento = movimento[COLUNA]

    #Posicao não é estável?
    if not posicoes_estaveis_posicao[l_movimento][c_movimento]:
        return False

    novo_add_posicao_estavel(movimento, posicoes_estaveis_posicao, the_board, color)

    lista_virados = [None,]

    for direction in the_board.DIRECTIONS:
        novos_virados = cria_lista_virados(the_board, movimento, color, direction, posicoes_estaveis_posicao)

        if novos_virados != [] and novos_virados != None:
            lista_virados.extend(novos_virados)
    ha_novo_estavel = True

    lista_virados.append(movimento)

    while(ha_novo_estavel and lista_virados != []):
        ha_novo_estavel = False
        lista_novos_estaveis = []

        for virado in lista_virados:
            estavel =  novo_verifica_add_posicao_estavel_capturadas(virado, posicoes_estaveis, the_board, color)
            ha_novo_estavel = ha_novo_estavel or estavel

            if(estavel):
                lista_novos_estaveis.append(virado)

        for novo_estavel in lista_novos_estaveis:
            lista_virados.remove(novo_estavel)

    return True

def novo_verifica_add_posicao_estavel_capturadas(movimento, posicoes_estaveis_posicao, the_board, color):
    if movimento is None:
        return False
    
    l_movimento = movimento[LINHA]
    c_movimento = movimento[COLUNA]

    #Posicao não é estável?
    if not posicoes_estaveis_posicao[l_movimento][c_movimento]:
        return False

    novo_add_posicao_estavel(movimento, posicoes_estaveis_posicao, the_board, color)

    return True

def cria_lista_virados(the_board, origin, color, direction, posicoes_estaveis_posicao):
        """
        Traverses the board in the given direction,
        transforming the color of appropriate tiles
        :param origin: where the traversal will begin
        :param color:
        :param direction:
        :return:
        """
        virados = []
        destination = the_board.find_bracket(origin, color, direction)  # move, player, board, direction)

        if not destination:
            return

        ox, oy = origin
        dx, dy = direction

        nx, ny = ox + dx, oy + dy  # n stands for 'next'

        while (nx, ny) != destination:
            # flips the tile and updates piece counts
            virados.append((nx, ny))
            nx, ny = nx + dx, ny + dy