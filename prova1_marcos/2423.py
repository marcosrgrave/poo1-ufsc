
# Alocando os ingredientes a um vetor
ingredientes = list(map(int, input().strip().split()))

# Definindo a quantidade necessária de cada ingrediente para conseguir fazer um bolo
bolo = [2, 3, 5]


razao_ingredientes = []  # vetor em que serão armazenadas a razao entre a qtd de ingredientes existentes com a necessária
for i in range(0, 3):  # para cada ingrediente, faça:
    razao = ingredientes[i] // bolo[i]  # calculando a razao entre a qtd de ingredientes existentes com a necessária
    razao_ingredientes.append(razao)  # adicionando essa razao ao vetor criado

# Nao adianta ter 100 ovos caso só possua o mínimo dos demais ingredientes, pois só dará pra fazer um único bolo
# Por isso, o fator determinante de quantos bolos serão feitos será a menor razao encontrada
print(min(razao_ingredientes))
