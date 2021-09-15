import copy


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

def posicao_segura_esq_dir(posicoes_estaveis_posicao, l1, l2, c1, c2, color, the_board):
    condicao1_estavel = posicoes_estaveis_posicao[l1][c1] and posicoes_estaveis_posicao[l1][c2]
    condicao1_cor     = the_board.tiles[l1][c1] == color  and the_board.tiles[l1][c2] == color

    condicao2_estavel = posicoes_estaveis_posicao[l2][c1] and posicoes_estaveis_posicao[l2][c2]
    condicao2_cor     = the_board.tiles[l2][c1] == color  and the_board.tiles[l2][c2] == color

    return (condicao1_estavel and condicao1_cor) or (condicao2_estavel and condicao2_cor)

def posicao_segura_cima_baixo(posicoes_estaveis_posicao, l1, l2, c1, c2, color, the_board):
    condicao1_estavel = posicoes_estaveis_posicao[l1][c1] and posicoes_estaveis_posicao[l2][c1]
    condicao1_cor     = the_board.tiles[l1][c1] == color  and the_board.tiles[l1][c2] == color

    condicao2_estavel = posicoes_estaveis_posicao[l1][c2] and posicoes_estaveis_posicao[l2][c2]
    condicao2_cor     = the_board.tiles[l2][c1] == color  and the_board.tiles[l2][c2] == color

    return (condicao1_estavel and condicao1_cor) or (condicao2_estavel and condicao2_cor)




def novo_add_posicao_estavel(movimento, posicoes_estaveis_posicao, the_board, color):
    l_movimento = movimento[LINHA]
    c_movimento = movimento[COLUNA]
    #É estável:
    esq = c_movimento-1
    dir = c_movimento+1
    cima = l_movimento-1
    baixo = l_movimento+1

    dir_cima_baixo = dir <= 7 and cima >= 0 and baixo <= 7
    esq_cima_baixo = esq >=0 and cima >= 0 and baixo <= 7
    esq_cima_dir = esq >=0 and cima >= 0 and dir <= 7 
    esq_baixo_dir = esq >=0 and baixo <= 7 and dir <= 7 

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
            if posicao_segura_esq_dir(posicoes_estaveis_posicao, baixo, cima, esq, c_movimento, color, the_board):
                posicoes_estaveis_posicao[l_movimento][esq] = True
                valor_tabuleiro[l_movimento][esq] = POSICAO_ESTAVEL
        #Verifíca se a posição da direita é estável
            elif dir_cima_baixo:
                if posicao_segura_esq_dir(posicoes_estaveis_posicao, baixo, cima, dir, c_movimento, color, the_board):
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
            if posicao_segura_cima_baixo(posicoes_estaveis_posicao, cima, l_movimento, esq, dir, color, the_board):
                posicoes_estaveis_posicao[cima][c_movimento] = True
                valor_tabuleiro[cima][c_movimento] = POSICAO_ESTAVEL
        #Verifíca se a posição de baixo é estável
        elif esq_baixo_dir:
            if posicao_segura_cima_baixo(posicoes_estaveis_posicao, baixo, l_movimento, esq, dir, color, the_board):
                posicoes_estaveis_posicao[baixo][c_movimento] = True
                valor_tabuleiro[baixo][c_movimento] = POSICAO_ESTAVEL

    return posicoes_estaveis_posicao

def novo_verifica_add_posicao_estavel(movimento, posicoes_estaveis_posicao, the_board, color, print_valores=False):
    lista_virados = [movimento,]
    new_board = copy.deepcopy(the_board)

    px, py = movimento
    new_board.tiles[px][py] = color
    new_board.piece_count[color] += 1
    new_board.piece_count[new_board.EMPTY] -= 1


    for direction in new_board.DIRECTIONS:
        virados = cria_lista_virados(new_board, (movimento[1], movimento[0]), color, direction)

        if virados != [] and virados != None:
            lista_virados.extend(virados)
        
        virados = []

    if print_valores:
        print("=========>", lista_virados)

    #me_ajuda = False
    #if((0,6) in lista_virados):
    #    me_ajuda = True

    ficou_estavel = True
    cont = 0

    while(ficou_estavel and lista_virados != [] and lista_virados != None):
        ficou_estavel = False
        virados_estaveis = []
        
        for virado in lista_virados:
            eh_estavel, posicoes_estaveis_posicao = add_virados_estaveis(virado, posicoes_estaveis_posicao, the_board, color)

            if eh_estavel:
                virados_estaveis.append(virado)
                cont += 1

            ficou_estavel = ficou_estavel or eh_estavel
        
        for estavel in virados_estaveis:
            lista_virados.remove(estavel)

        '''print("Estaveis::::::::::::", virados_estaveis)
        print("Nova lista::::::::::::", lista_virados)'''


    if print_valores:
        print("\n\n***************")
        for p in posicoes_estaveis_posicao:
            print(p)
        print("***************\n\n")

    if cont == 0:
        return (False, posicoes_estaveis_posicao)
     
    return (True, posicoes_estaveis_posicao)

def add_virados_estaveis(movimento, posicoes_estaveis_posicao, the_board, color):
    l_movimento = movimento[LINHA]
    c_movimento = movimento[COLUNA]

    #Posicao não é estável?
    if not posicoes_estaveis_posicao[l_movimento][c_movimento]:
        return (False, posicoes_estaveis_posicao)

    posicoes_estaveis_posicao = novo_add_posicao_estavel(movimento, posicoes_estaveis_posicao, the_board, color)

    return (True, posicoes_estaveis_posicao)

def cria_lista_virados(the_board, origin, color, direction):
    """
    Traverses the board in the given direction,
    transforming the color of appropriate tiles
    :param origin: where the traversal will begin
    :param color:
    :param direction:
    :return:
    """
    
    destination = the_board.find_bracket(origin, color, direction)  # move, player, board, direction)
    virados = []

    if not destination:
        return virados

    ox, oy = origin
    dx, dy = direction

    nx, ny = ox + dx, oy + dy  # n stands for 'next'

    opp = the_board.opponent(color)

    while (nx, ny) != destination:
        # flips the tile and updates piece counts
        the_board.tiles[nx][ny] = color
        the_board.piece_count[color] += 1
        the_board.piece_count[opp] -= 1

        virados.append((ny, nx))
        nx, ny = nx + dx, ny + dy        
    
    virados.append((destination[1], destination[0]))

    return virados