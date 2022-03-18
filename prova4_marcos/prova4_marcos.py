
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

            # verificando cada carta base nas que sobraram e adicionando ao contador
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

    def duas_notas():
        pass


RespostasProva4.duas_notas()
# cd prova4_marcos
# python prova4_marcos.py < inputs_prova4.txt