# Alocando as idades em variáveis
age1 = int(input())
age2 = int(input())

# Definindo as 3 principais regras e alocando-as a variaveis correspondentes
child = age1 < 6 or age2 < 6
adult = age1 >= 18 or age2 >= 18
teenager = age1 >= 14 and age2 >= 14

# Permitindo a entrada ou não com base nas 3 regras anteriores
print('YES') if adult and not child or teenager else print('NO')
