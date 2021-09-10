import random
import copy
import sys
sys.path.append('..')  # i know this is a dirty hack but, you know, time...
import board

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

INFINITO_POSITIVO = float('inf')
INFINITO_NEGATIVO = float('-inf')
VALOR             = 0
MOVIMENTO         = 1

#Heurística
def avalia(movimento, the_board, color, enemy_color):
    return (10, movimento)

#Profundidade
def teste_corte(movimento, the_board, color, enemy_color):
    
    '''
    #Avalia se é um estado final ou não
    if(b.is_terminal_state()):
        print("Acabou!!")
    else:
        print("Ainda não acabou!")
    '''

    #Teste que verifica se o jogo acaba nesse estado
    if(movimento != None):
        return True
    
    return False


def valor_min(movimento, alfa, beta, the_board, color, enemy_color):
    if teste_corte(movimento, the_board, color, enemy_color):
        return avalia(movimento, the_board, color, enemy_color)
    
    v = []*2

    v[VALOR] = INFINITO_POSITIVO
    v[MOVIMENTO] = None

    new_board = copy.deepcopy(the_board)

    if movimento != None:
        new_board.process_move(movimento, color)

    sucessores = new_board.legal_moves(color)

    for proximo_movimento in sucessores:
        v_max = valor_max(proximo_movimento, alfa, beta, new_board, enemy_color, color)

        if min(v[VALOR], v_max[VALOR]) == v_max[VALOR]:
            v[VALOR] = v_max[VALOR]
            v[MOVIMENTO] = proximo_movimento

        beta = min(beta, v[VALOR])

        if beta <= alfa:
            break
    
    return v

def valor_max(movimento, alfa, beta, the_board, color, enemy_color):
    if teste_corte(movimento, the_board, color, enemy_color):
        return avalia(movimento)
    
    v = [INFINITO_NEGATIVO, None]

    #v[VALOR] = INFINITO_NEGATIVO
    #v[MOVIMENTO] = None

    new_board = copy.deepcopy(the_board)

    if movimento != None:
        new_board.process_move(movimento, color)

    sucessores = new_board.legal_moves(color)

    for proximo_movimento in sucessores:
        v_min = valor_min(proximo_movimento, alfa, beta, new_board, enemy_color, color)
        if max(v[VALOR], v_min[VALOR]) == v_min[VALOR]:
            v[VALOR] = v_min[VALOR]
            v[MOVIMENTO] = proximo_movimento
        
        alfa = max(alfa, v[VALOR])

        if alfa >= beta:
            break

    return v

def decisao_minimax_alfa_beta(the_board, color, enemy_color):
    new_board = copy.deepcopy(b)
    v = valor_max(None, INFINITO_NEGATIVO, INFINITO_POSITIVO, new_board, color, enemy_color)

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


