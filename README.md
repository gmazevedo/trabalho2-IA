# Inteligência Artificial - Trabalho 2
O objetivo do deste trabalho é explorar a implementação de poda alfa-beta (com algoritmo Minimax) a partir da  implementação de um agente capaz de jogar Othello (também conhecido como Reversi).

## Integrantes do grupo
- Gessica Franciéle Mendonça Azevedo - 302865  - Turma A  
- Rafael Oleques Nunes - 309114 - Turma B
- Tatiane Sequerra Stivelman - 243681  - Turma B

## Descrição do algoritmo - funções
> Para fazer a avaliação do próximo movimento foram usadas as seguintes heurísticas:
- Posição do tabuleiro: cada posição do tabuleiro tem um valor, por exemplo: os cantos são considerados posições estáveis, então recebem valor 4, as posições ao redor dos cantos são perigosas, então tem valores negativos.
- Comparação mobilidade: retorna a diferença entre a quantidade de movimentos legais do jogador e do oponente.
- Risco de captura: se o movimento avaliado deixar uma peça numa posição onde possa ser capturada no movimento logo depois, retorna negativo, senão, positivo
- Quantidade de peças capturadas: retorna quantas peças do oponente o jogador irá capturar se fizer o movimento avaliado.
- Posição estável: retorna 1000 para posições estáveis e 0 para as que não forem.
> Foram usadas as seguintes estratégias de parada:
- Limite de tempo: a execução da função é encerrada no momento que dura mais que 1 segundo.
- Limite de profundidade: na busca do valor max, a profundidade máxima da busca é 50 e na busca do valor min, a profundidade máxima da busca é 49.
## Melhorias feitas (?)
> eventuais melhorias (quiescence search, singular extensions, etc);
## Decisões de projeto
> decisões de projeto e dificuldades encontradas;
## Bibliografia
> bibliografia completa (incluindo sites).
