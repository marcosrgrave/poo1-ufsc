# Estrutura de repetição que só irá encerrar quando o input 'number_of_matches' for igual a zero
c = 0
c_list = []
result = []
while True:
    number_of_matches = int(input())  # input
    if number_of_matches == 0:  # a flag corresponde a zero, neste caso
        break
    
    # Recebendo o input da diferença dos gols e armazenando-o em uma lista
    goal_dif_list = []
    for match in range(0, number_of_matches):
        match_result = input().strip().split()
        goals_scored, goals_taken = int(match_result[0]), int(match_result[1])
        goal_dif = goals_scored - goals_taken
        goal_dif_list.append(goal_dif)

    # Armazenando a maior diferença encontrada na lista
    best_dif = max(goal_dif_list)
    
    # Caso a diferença seja menor ou igual a zero, mostre a resposta 'nenhum'
    if best_dif <= 0:
        result.append('nenhum')
    
    # Caso contrário, pegue a posição de 'best_dif' na lista em ordem crescente e descendente, respectivamente
    else:
        up = goal_dif_list.index(best_dif)
        down = len(goal_dif_list)-1 - list(reversed(goal_dif_list)).index(best_dif)
        result.append([up+1, down+1])
    
    c += 1
    c_list.append(c)

# Printando as respostas armazenadas
for i, r in enumerate(result):
    print(f'Teste {c_list[i]}\n{r[0]} {r[1]}\n') if len(r)<=2 else print(f'Teste {c_list[i]}\n{r}\n')


# Inputs de Teste | Preciso arrumar o teste de numero 5
# 2
# 2 3
# 7 1
# 9
# 2 2
# 0 5
# 6 2
# 1 4
# 0 0
# 5 1
# 1 5
# 6 2
# 0 5
# 3
# 0 2
# 0 3
# 0 4
# 6
# 2 3
# 7 1
# 234 6536
# 21 6
# 15 1241
# 123 636
# 9
# 2 2
# 0 5
# 6 2
# 1 4
# 0 0
# 5 1
# 1 5
# 6 2
# 5 0
# 3
# 2 2
# 3 3
# 4 4
# 0