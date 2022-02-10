def peca_perdida():  # Ok
    # adicionando todas as peças em uma lista
    N : int = int(input())
    pecas_totais : list = list()
    for v in range(1, N+1):
        pecas_totais.append(v)

    # input de peças que não estão faltando
    pecas_presentes : list = list(map(int, input().split()))

    # verificando qual peça que está faltando
    for peca in pecas_totais:
        if peca not in pecas_presentes:
            peca_faltando = peca
            return print(peca_faltando)


def semente():
    # inputs exercicio
    tamanho_fita, qtd_gotas_iniciais = map(int, input().split())
    posicao_gotas_iniciais = list(map(int, input().split()))

    # criando uma fita repleta de espacos vazios. Sem Gota = 0; Com Gota = 1
    fita : list = []
    for espacos_vazio in range(tamanho_fita):
        fita.append(0)
    fita_adicionados_dia = fita  # repleta de vazios. só vai receber as gotas adicionadas no dia

    # colocando as gotas inicias na fita
    for i in posicao_gotas_iniciais:
        fita[i-1] = 1
    
    dia = 0
    fita_adicionados_dia = fita[:]
    while 0 in fita:
        dia += 1
        for i, gota in enumerate(fita_adicionados_dia):
            if gota == 1:
                if i == 0:
                    fita[i+1] = 1  # add_depois
                    fita_adicionados_dia[i] = 0
                    fita_adicionados_dia[i+1] = 1
                elif i == len(fita)-1:
                    fita[i-1] = 1  # add_antes
                    fita_adicionados_dia[i] = 0
                    fita_adicionados_dia[i-1] = 1
                else:
                    fita[i-1] = 1  # add_antes
                    fita_adicionados_dia[i] = 0
                    fita_adicionados_dia[i-1] = 1

                    fita[i+1] = 1  # add_depois
                    fita_adicionados_dia[i] = 0
                    fita_adicionados_dia[i+1] = 1
            print(fita_adicionados_dia)


def loteria():  # Ok
    # inputs exercicio
    premios = ['terno', 'quadra', 'quina', 'sena']
    aposta = list(map(int, input().split()))
    numeros_sorteados = list(map(int, input().split()))

    # calculando quantos numeros ele acertou    
    total_acertos = 0
    for numero in numeros_sorteados:
        if numero in aposta:
            total_acertos += 1
     
    # mostrando o resultado final
    print('azar') if total_acertos < 3 else print(premios[total_acertos-3])


def states_north():  # Ok
    # inputs
    estados_norte_brasil = ['roraima', 'acre', 'amapa', 'amazonas', 'para', 'rondonia', 'tocantins']
    estado = input()

    # verificando se o estado está na regiao norte e mostrando o resultado
    print('Regiao Norte') if estado in estados_norte_brasil else print('Outra regiao')


def command_history():
    # será feita a repetição até que a quantidade de comandos a serem analsiados seja nula
    while True:
        
        # inputs
        qtd_comandos = int(input())
        if qtd_comandos == 0:
            break
        historico_incial = list(map(int, input().split()))
        
        # definindo variáaveis e dando valores inciais
        historico_repetido = []
        soma = 0
        flag = False
        
        # caso o comando não esteja no histórico, soma-se até a posição dele
        # caso esteja no histórico incial, soma-se apenas até a posição do valor no histórico repetido
        for comando in historico_incial:
            for comando_repetido in historico_repetido:
                if comando_repetido == comando:
                    soma += 1
                    flag = True
                    break
                else:
                    soma += 1
            
            # adicionando o comando acionado ao historico de comandos repetidos
            historico_repetido.insert(0, comando)

            # se o comando digitado nao estiver no historico repetido, basta somar a posicao do proprio comando
            # caso contrario, nao é somado nada, repetindo o loop p/ analisar o proximo comando desejado
            if not flag:
                soma += comando
            else:
                continue
        
        # mostrando o resultado da soma encontrada
        print(soma)


def encrypted():
    pass


def santas_toys():  # Ok
    # input para o loop exato de leitura
    qtd_nao_enviaram = int(input())
    
    # estabelecendo valores iniciais às variáveis
    carrinhos = bonecas = 0

    # lendo os dados referentes às crianças
    for crianca in range(qtd_nao_enviaram):
        nome, sexo = input().split()
        if sexo in 'mM':
            carrinhos += 1
        else:
            bonecas += 1
    
    # mostrando o resultado das somas
    print(f'{carrinhos} carrinhos\n{bonecas} bonecas')


def pares_numeros():  # Ok
    # inputs iniciais
    qtd_int, min_sum, max_sum = map(int, input().split())
    inteiros = list(map(int, input().split()))

    # iniciando contandor
    qtd_pares = 0

    # a ideia foi fixar o primeiro numero e compará-lo com todos os demais (os que "variam")
    for i_fixo, n_fixo in enumerate(inteiros):
        for i_var in range(i_fixo+1, len(inteiros)):
            
            # estabelecendo os numeros que ficam variando para comparação com o 'n_fixo'
            n_var = inteiros[i_var]

            # considerando o par apenas se a condição for satisfeita
            if min_sum <= (n_fixo + n_var) <= max_sum:
                qtd_pares += 1
    
    # mostrando a quantidade de pares encontrados
    print(qtd_pares)


def text_correction():
    pass


def class_dismissed():
    pass


def correct_answers():
    pass


def mini_poker():
    pass


def lunar_temperature():
    pass



class_dismissed()