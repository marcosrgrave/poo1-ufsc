# Inputs
B = int(input())
T = int(input())

# Dimensoes da nota de 100 reais
h_nota = 70
b_nota = 160

# Calculo da area resultada pelo corte
area_corte = (B+T)*h_nota/2

# Casos possiveis
if area_corte == h_nota*b_nota/2:  # quando a area do corte for igual a metade da area da nota
    print(0)
else:    
    vale100 = area_corte > h_nota*b_nota/2  # Booleano indicando se a area do corte vale 100 reais ou nao
    print(1) if vale100 else print(2)
