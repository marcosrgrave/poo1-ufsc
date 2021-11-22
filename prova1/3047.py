# Inputs
idade_monica = int(input())
idade_filho1 = int(input())
idade_filho2 = int(input())

# Econtrando a idade do outro filho
outro_filho = idade_monica - (idade_filho1 + idade_filho2)

# Definindo o filho mais velho
filho_mais_velho = max(idade_filho1, idade_filho2, outro_filho)

# Output
print(filho_mais_velho)
