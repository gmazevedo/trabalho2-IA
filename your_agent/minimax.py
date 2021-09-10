INFINITO_NEGATIVO  = -100000
INFINITO_POSITIVO  =  100000

def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    TAMANHO = 9
    
    posicao = estado.index("_")
    possibilidades = []

    #Baixo
    if posicao + 3 < TAMANHO:
        novo_estado = estado

        posicao_movimento = posicao+3

        str_trocada = novo_estado[posicao_movimento]
        novo_estado = novo_estado.replace(novo_estado[posicao_movimento], "*")
        novo_estado = novo_estado.replace(novo_estado[posicao], str_trocada)
        novo_estado = novo_estado.replace(novo_estado[posicao_movimento], "_")

        possibilidades.append(("abaixo", novo_estado))

    #Cima
    if posicao -3 >= 0:
        novo_estado = estado

        posicao_movimento = posicao-3

        str_trocada = novo_estado[posicao_movimento]
        novo_estado = novo_estado.replace(novo_estado[posicao_movimento], "*")
        novo_estado = novo_estado.replace(novo_estado[posicao], str_trocada)
        novo_estado = novo_estado.replace(novo_estado[posicao_movimento], "_")

        possibilidades.append(("acima", novo_estado))

    #Direita
    if posicao + 1 < TAMANHO and (posicao + 1) %3 != 0:
        novo_estado = estado

        posicao_movimento = posicao+1

        str_trocada = novo_estado[posicao_movimento]
        novo_estado = novo_estado.replace(novo_estado[posicao_movimento], "*")
        novo_estado = novo_estado.replace(novo_estado[posicao], str_trocada)
        novo_estado = novo_estado.replace(novo_estado[posicao_movimento], "_")

        possibilidades.append(("direita", novo_estado))
    
    #Esquerda
    if posicao - 1 >= 0 and posicao %3 != 0:
        novo_estado = estado

        posicao_movimento = posicao-1

        str_trocada = novo_estado[posicao_movimento]
        novo_estado = novo_estado.replace(novo_estado[posicao_movimento], "*")
        novo_estado = novo_estado.replace(novo_estado[posicao], str_trocada)
        novo_estado = novo_estado.replace(novo_estado[posicao_movimento], "_")

        possibilidades.append(("esquerda", novo_estado))
    
    return possibilidades

def espande(estado, v):
    NotImplemented

#Heurística
def avalia(estado):
    NotImplemented

#Profundidade
def teste_corte(estado):
    NotImplemented

def valor_max(estado, alfa, beta):
    if teste_corte(estado):
        return avalia(estado)
    
    v = INFINITO_NEGATIVO

    sucessores = espande(estado)

    for sucessor in sucessores:
        v = max(v, valor_min(sucessor, alfa, beta))
        alfa = max(alfa, v)

        if alfa >= beta:
            break
    
    return v

def valor_min(estado, alfa, beta):
    if teste_corte(estado):
        return avalia(estado)
    
    v = INFINITO_POSITIVO

    sucessores = espande(estado)

    for sucessor in sucessores:
        v = min(v, valor_max(sucessor, alfa, beta))
        beta = min(beta, v)

        if beta <= alfa:
            break
    
    return v

def decisao_minimax_alfa_beta(estado):
    v = valor_max(estado, INFINITO_NEGATIVO, INFINITO_POSITIVO)

    #Retorna a acao en sucessores(estado) com v
    NotImplemented