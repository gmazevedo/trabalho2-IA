# Inteligência Artificial - Trabalho 2
O objetivo do deste trabalho é explorar a implementação de poda alfa-beta (com algoritmo Minimax) a partir da  implementação de um agente capaz de jogar Othello (também conhecido como Reversi).

## Integrantes do grupo
- Gessica Franciéle Mendonça Azevedo - Turma A  
- Rafael Oleques Nunes - Turma B
- Tatiane Sequerra Stivelman - Turma B

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
## Decisões de projeto
A ideia era incluir mais heurísticas, como a verificação de "paredes" na hora de calcular o custo de uma jogada, porém não foi possível implementar pois não chegamos a um código funcional para isso. Também não foi feito nenhuma otimização, por conta da complexidade e também pelo tempo pouco disponível pelos integrantes para poder dedicar ao trabalho, o foco foi fazer o agente ser funcional.
## Bibliografia
> Sites utilizados como base para implementação de estratégias.
- Othello - Reversi : MC906 - Introdução à Inteligência Artificial  
https://www.ic.unicamp.br/~rocha/teaching/2011s2/mc906/seminarios/2011s2-mc906-seminario-04.pdf

- How to win at Othello? Part 1 – Strategy basics, stable discs and mobility  
https://bonaludo.com/2017/01/04/how-to-win-at-othello-part-1-strategy-basics-stable-discs-and-mobility/
