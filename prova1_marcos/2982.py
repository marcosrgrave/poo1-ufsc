# OBS: No exercício em inglês diz para printar o que está na linha 13 (em inglês)
# Contudo, ao testar a solução, percebe-se que exige o print da linha 14 (em português)

# Input inicial
qtd_valores = int(input())

sum = 0  # é definida a soma inicial como nula para não haver erro no método de adição futuro (somando ela mesma)
for valor in range(0, qtd_valores):  # para cada valor da pauta, faça:
    char, numero = input().strip().split()  # alocando os inputs do valor em variaveis
    sum = sum + int(numero) if char == 'V' else sum - int(numero)  # a soma aumenta se é depositado verba e diminui se são apresentados os custos da universidade

# Printando um resultado no caso da soma ser positiva, ou outro se negativa.
# print('The strike will stop.') if sum > 0 else print('NO CUT, FIGHT!')
print('A greve vai parar.') if sum > 0 else print('NAO VAI TER CORTE, VAI TER LUTA!')
