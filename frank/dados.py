MEIO = 15
QUADRADO_X = -10
PERIGOSO = -20
POSICAO_ESTAVEL = 100

CANTO_1 = 0
CANTO_2 = 7

#Posições estáveis iniciais

posicoes_estaveis = [([False]*8) for i in range(8)]
posicoes_estaveis[0][0] = True
posicoes_estaveis[0][7] = True
posicoes_estaveis[7][0] = True
posicoes_estaveis[7][7] = True

#Valor padrão das posições
valor_tabuleiro = [[POSICAO_ESTAVEL,     PERIGOSO,  2, 2, 2, 2, PERIGOSO,  POSICAO_ESTAVEL],
                   [PERIGOSO,            QUADRADO_X,-1,-1,-1,-1, QUADRADO_X,PERIGOSO],
                   [2,                   -1,         1, 0, 0, 1, -1,        2],
                   [2,                   -1,         0, 1, 1, 2, -1,        2],
                   [2,                   -1,         0, 1, 1, 2, -1,        2],
                   [2,                   -1,         1, 0, 0, 1, -1,        2],
                   [PERIGOSO,            QUADRADO_X,-1,-1,-1,-1,QUADRADO_X,PERIGOSO],
                   [POSICAO_ESTAVEL,     PERIGOSO,   2, 2, 2, 2,PERIGOSO,  POSICAO_ESTAVEL]]
