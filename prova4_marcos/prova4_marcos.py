
class RespostasProva4:

    def truco_da_galera():  # Ok
        # inputs iniciais
        qtd_casos = int(input())
        cartas_base = ["Q", "K", "J", "A"]

        # para cada caso
        for n in range(qtd_casos):
            cartas_sobraram = input()

            # contador da presença das cartas base nas cartas que sobraram
            s = 0

            # verificando cada carta base nas que sobraram
            # e adicionando ao contador
            for carta in cartas_base:
                if carta in cartas_sobraram:
                    s += 1

            # mostrando resultado final
            print("Aaah muleke") if s >= 4 else print("Ooo raca viu")

    def grupo_trabalho_noel():  # Ok
        # input inicial
        qtd_elfos = int(input())

        # organizando as horas necessárias para cada grupo
        grupos_horas = {
            "bonecos": 8,
            "arquitetos": 4,
            "musicos": 6,
            "desenhistas": 12
        }

        # organizando as somas das horas aplicadas pelos elfos
        grupos_soma = {
            "bonecos": 0,
            "arquitetos": 0,
            "musicos": 0,
            "desenhistas": 0
        }

        # em cada entrada, somar as horas aplicadas ao respectivo grupo
        for entrada in range(qtd_elfos):
            nome_elfo, grupo, horas_aplicadas = input().split()
            grupos_soma[grupo] += int(horas_aplicadas)

        # calculando o total de brinquedos feitos para cada grupo
        total_brinquedos = 0
        for grupo in grupos_horas.keys():
            horas_necessarias = grupos_horas[grupo]
            horas_totais = grupos_soma[grupo]
            total_brinquedos += horas_totais // horas_necessarias

        # mostrando o resultado final
        print(total_brinquedos)

    def tomadas_eletricas():  # Ok
        # input inicial
        qtd_testes = int(input())

        for teste in range(qtd_testes):
            entrada: list = list(map(int, input().split()))

            # organizando os dados do input principal
            qtd_filtros_linha: int = entrada[0]
            tomadas_em_cada_filtro: list = entrada[1:]

            # calculado a qtd de aparelhos que serao alimentados
            qtd_aparelhos_alimentados: int = sum(
                tomadas_em_cada_filtro) - (qtd_filtros_linha - 1)

            # mostrando os resultados
            print(qtd_aparelhos_alimentados)

    def domino():  # Ok
        # input do tipo do jogo
        tipo_jogo: int = int(input())

        # somando a quantidade de peças do tipo de jogo informado
        s = 0
        for n in range(tipo_jogo+1, 0, -1):
            s += n

        # mostrando o resultado encontrado
        print(s)

    def tijolao():  # Ok

        # dicionario das teclas
        teclas_pressionadas: dict = {
            "a": 1 * "2",
            "b": 2 * "2",
            "c": 3 * "2",

            "d": 1 * "3",
            "e": 2 * "3",
            "f": 3 * "3",

            "g": 1 * "4",
            "h": 2 * "4",
            "i": 3 * "4",

            "j": 1 * "5",
            "k": 2 * "5",
            "l": 3 * "5",

            "m": 1 * "6",
            "n": 2 * "6",
            "o": 3 * "6",

            "p": 1 * "7",
            "q": 2 * "7",
            "r": 3 * "7",
            "s": 4 * "7",

            "t": 1 * "8",
            "u": 2 * "8",
            "v": 3 * "8",

            "w": 1 * "9",
            "x": 2 * "9",
            "y": 3 * "9",
            "z": 4 * "9",

            " ": 1 * "0"
        }

        # input casos
        qtd_casos: int = int(input())

        # verificando cada letra da palavra e fazendo a devida formatacao
        # os resultados sao mostrados ao longo da execucao do loop
        for caso in range(qtd_casos):
            palavra = input()
            ultimo_numero = -1
            for char in palavra:
                numeros = teclas_pressionadas[char.lower()]
                if char.isupper():
                    print("#", end="")
                else:
                    if ultimo_numero == numeros[0]:
                        print("*", end="")
                ultimo_numero = numeros[0]
                print(numeros, end="")
            print()

    def duas_notas():  # Ok
        # definicao inicial
        notas_disponíveis = 2, 5, 10, 20, 50, 100

        # loop até EOF
        while True:

            # input dos valores
            valor_compra, valor_pago = map(int, input().split())

            # condicao para encerrar loop
            if valor_compra == 0 and valor_pago == 0:
                break

            # calculando troco a ser dado
            troco_inicial: int = valor_pago - valor_compra

            # definicoes para a condicao do exercicio
            troco_exato: bool = False
            troco: int = troco_inicial
            troco_temp: int = 0
            notas_utilizadas: int = 0

            # loop com cada nota disponivel para troco
            # se possivel troco, contabiliza as notas utilizadas
            for nota in sorted(notas_disponíveis, reverse=True):
                if (qtd_nota := troco // nota) > 0:
                    troco -= qtd_nota * nota
                    troco_temp += qtd_nota * nota
                    notas_utilizadas += 1

            # condicoes de existencias do troco em apenas duas notas
            cond1 = troco_inicial == troco_temp
            cond2 = notas_utilizadas == 2

            # mostrando resultado obtido
            print("possible") if cond1 and cond2 else print("impossible")

    def eachianosII():  # nao encerrada
        amount_tests: int = int(input())
        for test in range(amount_tests):
            txt: str = input()
            key: str = input()

            key_pos = start = 0
            while True:
                key_pos = txt.find(key, start)
                if key_pos == -1:
                    if start == 0:
                        print(key_pos)
                    break
                else:
                    start_word_index = key_pos
                    end_word_index = txt.find(" ", start_word_index)
                    word = txt[start_word_index:end_word_index]

                    if word != key:
                        start = end_word_index-1
                        continue
                    start = txt.find(" ", key_pos)
                    print(key_pos, end=" ")
            print()

    def o_retorno_do_rei():  # Ok, mas enviado após o horário da prova
        # input inicial
        qtd_runas, amizade_necessaria = map(int, input().split())

        # armazenando os nomes e valores das runas em um dicionario
        runas: dict = dict()
        for runa in range(qtd_runas):
            id_runa, amizade_runa = input().split()
            runas[id_runa] = int(amizade_runa)

        # inputs finais
        input()
        runas_utilizadas = input().split()

        # calculando os valores das runas utilizadas
        amizade_utilizada = 0
        for runa in runas_utilizadas:
            amizade_utilizada += runas[runa]

        # mostrando os resultados obtidos
        print(amizade_utilizada)
        if amizade_utilizada >= amizade_necessaria:
            print("You shall pass!")
        else:
            print("My precioooous")


RespostasProva4.eachianosII()
# cd prova4_marcos
# python prova4_marcos.py < inputs_prova4.txt
