# Alocando os inputs em variáveis
valor_compra = int(input())
num_parcelas = int(input())

# Caso 1: quando o resto é zero
if valor_compra % num_parcelas == 0:
    valor_parcelas = valor_compra // num_parcelas
    
    # Printando os valores das parcelas, que neste caso são iguais
    for i in range(0, num_parcelas):
        print(valor_parcelas)

# Caso 2: quando o resto não é zero
else:
    resto = valor_compra % num_parcelas  # alocando o resto em uma variável para utilizar na estrutura de repetição adiante
    valor_parcelas = valor_compra // num_parcelas  # pegando apenas o numero inteiro da parcela

    # Printando os valores das parcelas que possuem adicional de valor
    for i in range(0, resto):
        print(valor_parcelas+1)
    
    # Printando os valores das demais parcelas (sem adicional de valor)
    for i in range(0, num_parcelas-resto):
        print(valor_parcelas)
