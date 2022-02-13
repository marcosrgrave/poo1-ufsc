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


def semente():  # Nao termimei
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


def command_history():  # Nao termimei
    # será feita a repetição até que a quantidade de comandos a serem analasiados seja nula
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


def encrypted():  # Ok
    # loop até a ultima linha do arquivo de input
    while True:
        try:
            # inputs
            correto       = 'aeiou'
            criptografado = '@&!*#'
            txt = input()
            
            # descriptografando
            for char_cript, char_correto in zip(criptografado, correto):
                txt = txt.replace(char_cript, char_correto)
            
            # mostrando o texto descriptografado
            print(txt)

        # encerrando o loop depois de ler a ultima linha do arquivo
        except EOFError:
            break


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


def text_correction():  # Ok
    # inciando um loop que só vai encerrar depois de ler todas as linhas do arquivo de input
    while True:
        # vai realizar o loop enquanto não der erro
        try:
            # input texto
            txt = input().strip()
            
            # utilizando o replace pra corrigir o texto
            txt = txt.replace(' ,', ',')
            txt = txt.replace(' .', '.')
            
            # mostrando o texto corrigido
            print(txt)
        
        # vai encerrar o loop após ler a última linha
        except EOFError:
            break
        

def class_dismissed():  # Ok
    # inputs
    n_students, min_students = map(int, input().split())
    
    # contando a quantidade de alunos que chegaram a tempo da aula
    students_on_time = 0
    expected_arrival = list(map(int, input().split()))
    for time in expected_arrival:
        if time <= 0:
            students_on_time += 1
    
    # mostrando se haverá aula ou não
    print('YES') if students_on_time >= min_students else print('NO')


def correct_answers():  # Nao consegui entender nada
    qtd_questions = int(input)()
    answer = input()
    qtd_classmates = int(input())
    for m8 in range(qtd_classmates):
        pass


def mini_poker():  # Nao terminei
    # A fim de organização, optei por montar uma função para cada regra.
    # Todas as funções retornam a pontuação da regra, caso seja verdadeira.
    def regra1(mao):
        mao = sorted(mao)
        x = mao[0]
        if [x, x+1, x+2, x+3, x+4] == mao:
            return 200 + mao[0]
        else:
            return 0

    def regra2(mao):
        mao = sorted(mao)
        x = mao[0]
        y = mao[-1]
        if [x, x, x, x, y] == mao or [y, y, y, y, x] == mao:
            return 180 + x
        else:
            return 0

    def regra3(mao):
        mao = sorted(mao)
        x = mao[0]
        y = mao[-1]
        if [x, x, x, y, y] == mao or [y, y, y, x, x] == mao:
            return 180 + x
        else:
            return 0
    
    def regra4(mao):
        mao = sorted(mao)
        nao_repetidas = []  # terei x, y, z
        for carta in set(mao):
            nao_repetidas.append(carta)
        if len(nao_repetidas) != 3:
            return 0
        else:
            if cond1[:3] == mao[:3] or cond2[1:4] == mao[1:4] or cond3[2:] == mao[2:]:
                return 140 + x
            
            # x vai ser sempre a mediana para esse caso
            # if 3*x - (y+z) == sum(mao) - (y+z):
            #   return 140 + x  ... else return 0

            for x in nao_repetidas:  # x = carta
                cond1 = [x, x, x, y, z]# == mao or [x, x, x, z, y]
                cond2 = [y, x, x, x, z]# == mao or [z, x, x, x, y]
                cond3 = [y, z, x, x, x]# == mao or [z, y, x, x, x]
            # x, y, z = nao_repetidas[0], nao_repetidas[1], nao_repetidas[2]
            print(nao_repetidas)
            # sendo obrigatoriamente y != z, existem apenas 3 opções
            

    def regra5(mao):
        pass

    def regra6(mao):
        pass

    def regra7(mao):
        pass


    # def pares_trincas(mao):
    #     mao = sorted(mao)
    #     temp_soma = max_repetidas = min_repetidas = 0
    #     hist_soma = []
    #     for i in range(len(mao)-1):
    #         if mao[i] == mao[i+1]:
    #             temp_soma += 1
    #             hist_soma.append(temp_soma)
    #         else:
    #             temp_soma = 0
    #             hist_soma.append(temp_soma)
    #     print(hist_soma)

    #     # 1 em hist_soma corresponde a um par. 2 corresponde a uma trinca
    #     qtd_pares = qtd_trincas = qtd_quadras = qtd_quinas = 0
    #     jogos     = [0, 1, 2, 3, 4]  # 1 = par, 2 = trinca, 3 = quadra, 4 = quina
    #     qtd_jogos = [0, 0, 0, 0, 0]
    #     for value in hist_soma:
    #         i = jogos.index(value)
    #         qtd_jogos[i] += 1
    #     print(qtd_jogos)
    #     # só dá pra pegar como referencia o valor mais a direita
    


    # def repetidas(mao):
    #     qtd_carta_repetida = [0, 0, 0, 0, 0]
    #     for i, carta in enumerate(mao):  # set() só mostra as cartas nao repetidas
    #         if carta in set(mao):
    #             qtd_carta_repetida[i] += 1
    #     print(qtd_carta_repetida)
    
    n_jogadas = int(input())
    for jogada in range(n_jogadas):
        mao = list(map(int, input().split()))
        total_pontos = regra1(mao) + regra2(mao)
        print(mao)
        regra4(mao)


def lunar_temperature():  # Achar outra forma mais eficiente
    teste = 0
    while True:
        teste += 1

        qtd_medicoes, intervalo = map(int, input().split())
        if qtd_medicoes == intervalo == 0:
            break
        
        soma = cont = avg = 0
        max_avg = 0
        min_avg = 200
        for v in range(qtd_medicoes):
            n = int(input())
            if cont == 0 or intervalo == cont - intervalo:
                n0 = n
            soma += n
            cont += 1
            if cont == intervalo:
                avg = int(soma/cont)
                if avg > max_avg:
                    max_avg = avg
                if avg < min_avg:
                    min_avg = avg
                soma -= n0
                cont -= 1
            print(avg)


    # FUNCIONA, MAS TENHO QUE ENCONTRAR UM JEITO MAIS RAPIDO
    # teste = 0
    # while True:
    #     teste += 1

    #     qtd_medicoes, intervalo = map(int, input().split())
    #     if qtd_medicoes == intervalo == 0:
    #         break

    #     medicoes = []
    #     for v in range(qtd_medicoes):
    #         medicoes.append(int(input()))

    #     start = end = 0
    #     max_avg = 0
    #     min_avg = 200
    #     while end < len(medicoes):
    #         end = start + intervalo
    #         valores = medicoes[start:end]
    #         avg = int(sum(valores)/len(valores))

    #         if avg > max_avg:
    #             max_avg = avg
    #         if avg < min_avg:
    #             min_avg = avg
            
    #         start += 1

    #     print(f'Teste {teste}')
    #     print(min_avg, max_avg)
    #     print()
        



command_history()