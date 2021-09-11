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


