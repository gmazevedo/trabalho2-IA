import sys
from datetime import datetime

from frank.heuristicas import *

sys.path.append('..')  # i know this is a dirty hack but, you know, time...
import board

bd = {}

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

INFINITO_POSITIVO = float('inf')
INFINITO_NEGATIVO = float('-inf')

#Retorno do avanca
VALOR             = 0
MOVIMENTO         = 1
PROFUNDIDADE      = 2
ESTAVEL           = 3

#Limites para o teste de corte
LIMITE_MAX = 50
LIMITE_MIN = LIMITE_MAX - 1
LIMITE_TEMPO = 1

#Heurística
def avalia(movimento, the_board, color, enemy_color, profundidade, posicoes_estaveis_movimento, pontos_estavel):
    new_board = copy.deepcopy(the_board)
    
    if new_board.is_terminal_state():
        pontos_peca = heuristica_qtde_pecas_final(the_board, color, enemy_color)
        return (pontos_peca, movimento)
    
    #pontos_centro = heuristica_pecas_centros(new_board, color)
    #pontos_cantos = heuristica_peca_cantos(new_board, color)

    pontos_peca = heuristica_pecas_posicao(new_board, color, enemy_color)
    pontos_mobilidade = heuristica_comparacao_mobilidade(the_board, color, enemy_color)
    pontos_captura = heuristica_captura_aliado(the_board, enemy_color, movimento)
    pontos_qtd_pecas_capturadas = heuristica_qtde_pecas_capturadas(the_board, color, movimento)
    #pontos_posicao_estavel = heuristica_posicao_estavel(movimento, posicoes_estaveis_movimento)

    '''
    if pontos_posicao_estavel != 0:
        estavel = True
    else:
        estavel =False
    '''
    estavel = False

    pontos = pontos_peca + pontos_mobilidade + pontos_captura + pontos_qtd_pecas_capturadas + pontos_estavel

    return (pontos, movimento, profundidade, estavel)


#Profundidade
def teste_corte(movimento, the_board, color, enemy_color, profundidade, start_time, limite):
    
    '''
    #Avalia se é um estado final ou não
    if(b.is_terminal_state()):
        print("Acabou!!")
    else:
        print("Ainda não acabou!")
    '''

    stop_time = datetime.now() 
    duration = stop_time - start_time
    segundos = float(duration.total_seconds())

    if(segundos > LIMITE_TEMPO or profundidade > limite or the_board.is_terminal_state()):
        return True

    return False


def valor_min(movimento, alfa, beta, the_board, color, enemy_color, start_time, posicoes_estaveis_movimento, pontos_estavel, profundidade):
    if teste_corte(movimento, the_board, color, enemy_color, profundidade, start_time, LIMITE_MIN):
        return avalia(movimento, the_board, color, enemy_color, profundidade, posicoes_estaveis_movimento, pontos_estavel)

    v = [INFINITO_NEGATIVO, None, 0, False]

    new_board = copy.deepcopy(the_board)

    posicoes_estaveis_atual = copy.deepcopy(posicoes_estaveis_movimento)
    adicionou_estavel = False
    if movimento is not None:
        adicionou_estavel, posicoes_estaveis_atual = novo_verifica_add_posicao_estavel(movimento, posicoes_estaveis_atual, new_board, color)

    if adicionou_estavel:
        novos_pontos_estavel = pontos_estavel + 100
    else:
        novos_pontos_estavel = pontos_estavel

    if movimento != None:
        new_board.process_move(movimento, color)

    sucessores = new_board.legal_moves(color)

    for proximo_movimento in sucessores:
        if pula_comparacao(proximo_movimento, new_board, color):
            continue

        v_max = valor_max(proximo_movimento, alfa, beta, new_board, enemy_color, color, start_time, posicoes_estaveis_atual, novos_pontos_estavel, profundidade+1)

        if min(v[VALOR], v_max[VALOR]) == v_max[VALOR]:
            v[VALOR] = v_max[VALOR]
            v[MOVIMENTO] = proximo_movimento
            v[PROFUNDIDADE] = v_max[PROFUNDIDADE]
            v[ESTAVEL] = v_max[ESTAVEL]

        beta = min(beta, v[VALOR])

        if beta <= alfa:
            break
    
    return v


def valor_max(movimento, alfa, beta, the_board, color, enemy_color, start_time, posicoes_estaveis_movimento, pontos_estavel, profundidade=0):
    if teste_corte(movimento, the_board, color, enemy_color, profundidade, start_time, LIMITE_MAX):
        return avalia(movimento, the_board, color, enemy_color, profundidade, posicoes_estaveis_movimento, pontos_estavel)
        

    v = [INFINITO_NEGATIVO, None, 0, False]

    new_board = copy.deepcopy(the_board)

    posicoes_estaveis_atual = copy.deepcopy(posicoes_estaveis_movimento)
    adicionou_estavel = False
    if movimento is not None:
        adicionou_estavel, posicoes_estaveis_atual = novo_verifica_add_posicao_estavel(movimento, posicoes_estaveis_atual, new_board, color)

    if adicionou_estavel:
        novos_pontos_estavel = pontos_estavel + 100
    else:
        novos_pontos_estavel = pontos_estavel

    if movimento != None:
        new_board.process_move(movimento, color)
            
    sucessores = new_board.legal_moves(color)

    for proximo_movimento in sucessores:
        if pula_comparacao(proximo_movimento, new_board, color):
            continue

        v_min = valor_min(proximo_movimento, alfa, beta, new_board, enemy_color, color, start_time, posicoes_estaveis_atual, novos_pontos_estavel, profundidade+1)


        if max(v[VALOR], v_min[VALOR]) == v_min[VALOR]:
            v[VALOR] = v_min[VALOR]
            v[MOVIMENTO] = proximo_movimento
            v[PROFUNDIDADE] = v_min[PROFUNDIDADE]
            v[ESTAVEL] = v_min[ESTAVEL]
        
        alfa = max(alfa, v[VALOR])

        if alfa >= beta:
            break

    return v


def decisao_minimax_alfa_beta(the_board, color, enemy_color):
    global posicoes_estaveis
    new_board = copy.deepcopy(the_board)
    start_time = datetime.now()
    v = valor_max(None, INFINITO_NEGATIVO, INFINITO_POSITIVO, new_board, color, enemy_color, start_time, copy.deepcopy(posicoes_estaveis), 0, profundidade=0)

    x, posicoes_estaveis = novo_verifica_add_posicao_estavel(v[MOVIMENTO], posicoes_estaveis, new_board, color, print_valores=False)

    return v[MOVIMENTO]


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    if color == 'B':
        enemy_color = 'W'
    else:
        enemy_color = 'B'

    proximo_movimento = decisao_minimax_alfa_beta(the_board, color, enemy_color)

    
    return proximo_movimento

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta
    #return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])


if __name__ == '__main__':
    b = board.Board()
    print('Actual:')
    b.print_board()

    print("\n\n")

    move = make_move(b, 'B')
    print(f'A random move for black in the initial state: {move}')
    print('Resulting state:')
    b.process_move(move, 'B')
    b.print_board()


