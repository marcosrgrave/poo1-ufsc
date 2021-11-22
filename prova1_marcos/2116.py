# Obs: optei por tentar fazer com que o codigo aceitasse mais de 2 numeros no input.

# Alocando os numeros do input em uma lista
numeros = list(map(int, input().strip().split()))

# Processo de verificação para encontrar o primeiro numero primo
primo_list = []  # lista em que serão armazenados os numeros primos encontrados
for num in numeros:  # para cada numero do input, faça:
    primo_bool = False  # setando uma flag para encerrar o loop caso o primo seja encontrado
    for n1 in range(num, 0, -1):  # n1 representa o possível numero primo
        for n2 in range(n1-1, 0, -1):  # n2 seriam os valores anteriores a n1 para validar que n1 é de fato primo
            if n2 == 1:  # se ele chegar no 1 e o resto não ter sido zero, quer dizer que é primo, pois será divisível por 1 e por ele mesmo, apenas
                primo_bool = True  # flag booleana apenas para encerrar o loop de fora (n1) quando encontrar o primeiro primo e passar para o proximo 'num'
                primo_list.append(n1)  # adicionando o primo encontrado a uma lista
                break  # quebrando o loop de n2 após encontrado o primeiro numero primo
            elif n1 % n2 == 0:  # caso o resto da divisão seja zero, indica que o n1 não é primo
                break  # encerrando o loop de n2, pois foi verificado que n1 não é primo
        if primo_bool:  # essa quebra é para o programa não encontrar todos os demais primos, apenas o primeiro
            break

# Mutliplicando os numeros primos encontrados
mult = 1
for primo in primo_list:
    mult *= primo

print(mult)
