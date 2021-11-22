
# Inputs
marbles = int(input())
branches = int(input())

# Calculo da quantidade de bolinhas
needed_marbles = branches//2

# Verificando se irão faltar bolinhas ou não
faltam = True if needed_marbles - marbles > 0 else False

# Output
print(f'Faltam {needed_marbles - marbles} bolinha(s)') if faltam else print('Amelia tem todas bolinhas!')
