class Prova3:

    def inferior_area():  # Ok
        # input de soma ou média
        operation: str = input()
        
        # iniciando o somador dos valores e o contador para dividir a média
        soma: float = 0
        i: int = 0
        
        # passando por cada célula
        for line in range(0, 12):
            for column in range(0, 12):
                value: float = float(input())
                
                # condicoes do exercicio
                below_main_diagonal      : bool = line > column
                below_secondary_diagonal : bool = line > 11 - column
                
                # somando apenas as celulas que satisfizerem as condições acima
                if below_main_diagonal and below_secondary_diagonal:
                    i += 1
                    soma += value
        
        # exibindo o resultado conforme o input de soma ou média
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def counting_in_chinese():  # Ok
        # input qtd instancias
        n_instances : int = int(input())
        
        # lendo 1 matriz por instancia
        for n in range(n_instances):
            
            # criando vetores para armazenamento dos nao-nulos
            lines, columns, values = [], [], []

            # input da quantidade de linhas a serem analisadas
            N, rows = input().split()
            
            # lendo os dados da linha da matriz em questao 
            for r in range(int(rows)):

                # inputs dos dados da linha
                P, line, column, value = input().split()
                value = int(value)
                
                # realizando a soma do valor, caso a linha e a coluna já existam
                if line in lines and column in columns:
                    i = columns.index(column)
                    values[i] += value
                
                # caso a linha ou a coluna sejam novidade, adicionar todos os dados
                elif line not in lines or column not in columns:
                    lines.append(line)
                    columns.append(column)
                    values.append(value)

            # vetor de armazenamento da resposta final
            final_result = []
            
            # formatando os valores encontrados
            for non_null in range(len(lines)):
                i = non_null
                final_result.append(f'{lines[i]} {columns[i]} {values[i]}')
            resp = sorted(final_result)
            
            # mostrando as respostas encontradas
            for r in resp:
                print(r)
            
            # adicionando linha em branco apenas entre instâncias
            if n != n_instances - 1:
                print()


    def quadrado_magico():  # nao cheguei em nada
        # sum_line = sum_column = sum_diag1 = sum_diag2
        # 0 é o numero que precisa ser substituido
        
        sum_main_diag = sum_sec_diag = 0
        
        matrix = []
        sum_lines   = [[ ], [ ], [ ]]
        sum_columns = []
        stolen = []
        
        for l in range(3):
            line = list(map(int, input().split()))
            if 0 in line:
                stolen.append([l, line.index(0)])
            sum_lines[l] = sum(line)
            sum_main_diag += line[l]
            sum_sec_diag  += line[2-l]
            matrix.append(line)
        
        for i in range(3):
            sum_col = 0
            for line in matrix:
                sum_col += line[i]
            sum_columns.append(sum_col)
        
        print(matrix)
        print(sum_lines)
        print(sum_columns)
        print(sum_main_diag, sum_sec_diag)
        print(stolen)


    def frequencia_aula():  # Ok
        # total de alunos que respoderam presença
        qtd_presenca = int(input())
        
        # lista que armazenará as presencas
        presencas = []

        # adicionando as presencas à lista anterior
        for aluno in range(qtd_presenca):
            n_presenca = int(input())
            presencas.append(n_presenca)
        
        # obtendo a quantidade de alunos que tiveram presenca repetida
        alunos_repetidos = len(presencas) - len(set(presencas))
        
        total_alunos = len(presencas)
        
        # mostrando a resposta
        print(total_alunos - alunos_repetidos)


    def matrix_ladder():  # tá tudo errado nessa porra
        # cond1: only zeros
        qtd_lines, qtd_columns = map(int, input().split())
        cond1 = ok = False
        for line in range(qtd_lines):
            v_line = input().split()
            
            # condicao 1
            if cond1:
                if '123456789' not in v_line:
                    ok = True
                    print("cond1.1")
            elif '123456789' not in v_line:
                cond1 = True
                print("cond1.2")
            
            # condicao 2
            if not cond1:
                for i, v in enumerate(v_line):
                    if v != '0':
                        n_pos = i  # posicao primeiro numero diferente de zero
                        break
                if line == 0:
                    i_anterior = n_pos
                else:
                    if i_anterior > n_pos:
                        ok = True
                        i_anterior = n_pos
                    else:
                        ok = False
                        break
        
        print('S') if ok else print('N')


    def corredor():  # Ok (Kadane's Algorithm)
        
        # ---------------------------------------------------------

        # # CODIGO INICIAL (TIME LIMIT EXCEEDED)
        
        # # inputs iniciais
        # num_salas = input()
        # vetor = input().split()

        # # realiza a soma de todas as salas
        # # e vai removendo uma por vez, da esquerda para a direita
        # # registrando apenas a maior soma encontrada
        # maior_soma = 0
        # fim_loop = len(vetor)
        # for i1 in range(fim_loop):
        #     if int(vetor[i1]) > 0:
        #         soma = int(vetor[i1])
        #         for i2 in range(i1+1, fim_loop):
        #             soma += int(vetor[i2])
        #             if int(vetor[i2]) > 0 and soma > maior_soma:
        #                 maior_soma = soma
        
        # # mostrando a maior soma encontrada
        # print(maior_soma)

        # ---------------------------------------------------------
        
        # ALGORITMO PESQUISADO: Kadane's Algorithm
        # Nesse exercício tive que apelar para a Internet
        # Meu código inicial parecia resolver o problema, mas retornava Time Limit Exceeded
        # Encontrei o Kadane's Algorithm
        # https://en.wikipedia.org/wiki/Maximum_subarray_problem
        
        # inputs iniciais
        num_salas = input()
        vetor = list(map(int, input().split()))
        
        # Kadane's Algorithm
        # Achei a ideia do algoritmo semelhante ao do código inicial
        # Porém, ele nao necessita realizar dois loops, apenas um
        best_sum = 0
        current_sum = 0
        # aqui ele faz um loop para cada valor no vetor
        for x in vetor:
            # é feita a soma enquanto o current_sum é maior que zero
            # caso contrário, a soma é resetada
            current_sum = max(0, current_sum + x)
            # amazenando apenas a maior soma encontrada
            best_sum    = max(best_sum, current_sum)

        # mostrando o resultado
        print(best_sum)
                        

    def applying_tests():
        pass


    def coffee_harvest():  # Ok
        # loop até EOF
        while True:
            try:
                # inputs e definições iniciais
                qtd_rows, qtd_columns = map(int, input().split())
                bag_capacity : int = 60  # liters
                
                # soma acumulada de cada linha da matrix
                sum_matrix : int = 0
                for row in range(qtd_rows):
                    line : tuple = tuple(map(int, input().split()))
                    sum_matrix += sum(line)
                
                # calculo da quantidade de sacas e litros
                bags : int = sum_matrix//bag_capacity
                liters : int = sum_matrix - bags * bag_capacity
                
                # mostrando resultado formatado
                print(f'{bags} saca(s) e {liters} litro(s)')
            
            # encerrando loop quando for EOF
            except EOFError:
                break


    def battlefield():  # Ok
        # inputs iniciais
        height, width, n_soldiers = map(int, input().split())
        
        # razao entre a dimensao de largura com a altura da matrix
        wh_ratio = width / height

        # iniciando as somas que acumularao as habilidades dos soldados
        above_river = below_river = 0

        # loop de análise para cada soldado
        for soldier in range(n_soldiers):
            
            # inputs do soldado
            line, column, skill = map(int, input().split())
            
            # condicao para o soldado estar abaixo do rio
            if line > column / wh_ratio:
                below_river += skill
            
            # caso nao esteja abaixo, estará necessariamente acima do rio
            else:
                above_river += skill
        
        # mostrando os resultados
        print(above_river, below_river)


    def noise_effect():  # nao entendi a conta pra chegar no valor final
        print(10/16*100)
        while True:
            image_size : int = int(input())  # in pixels
            if image_size == 0:
                break
            
            standard_image : list = []
            scanned_image  : list = []
            
            def add_lines(vector):
                for row in range(image_size):
                    line : tuple = input().split()
                    vector.append(line)
            
            add_lines(standard_image)
            add_lines(scanned_image)
            
            # comparison
            pixels_ok = cont = max_confidence = 0
            for line_std, line_scnd in zip(standard_image, scanned_image):
                for v_std, v_scnd in zip(line_std, line_scnd):
                    # print(v_scnd, v_std)
                    if abs(int(v_scnd) - int(v_std)) <= 100:
                        pixels_ok += 1
                    cont += 1
                    confidence_degree : float = pixels_ok / cont
                    if confidence_degree > max_confidence:
                        max_confidence = confidence_degree
            
            div = image_size**2
            max_confidence *= 100
            
            print(f'{max_confidence:.2f}')
            print()


    def repeated_stickers():  # Ok
        # input quantidade de figurinhas
        n_stickers : int = int(input())
        
        # vetor para armazenar todas as figurinhas
        total_stickers : list = []

        # lendo o valor de cada figurinha e armazenando no vetor anterior
        for n in range(n_stickers):
            sticker : int = int(input())
            total_stickers.append(sticker)

        # encontrando as figurinhas unicas e as repetidas
        uniques = len(set(total_stickers))
        repeated  = len(total_stickers) - uniques

        # mostrando os valores encontrados
        print(uniques)
        print(repeated)


    def samuel_coffee_grower():  # Ok
        # importanto lib para operacoes matematicas
        from math import acos, degrees, sin, radians
        
        # vetor que armzenará a area do primeiro e do segundo terreno
        areas = []

        # loop para calculo da area de cada terreno
        for land in range(2):

            # definicao dos vertices do terreo
            xA, yA = map(int, input().split())
            xB, yB = map(int, input().split())
            xC, yC = map(int, input().split())
            xD, yD = map(int, input().split())

            # triangulo superior
            a  = ((xB - xD)**2 + (yB - yD)**2)**(1/2)  # segmento do vertice B ao D
            b1 = ((xA - xD)**2 + (yA - yD)**2)**(1/2)  # segmento do vertice A ao D
            d1 = ((xB - xA)**2 + (yA - yB)**2)**(1/2)  # segmento do vertice A ao B

            # triangulo inferior
            c = a
            b2 = ((xC - xD)**2 + (yC - yD)**2)**(1/2)  # segmento do vertice C ao D
            d2 = ((xB - xC)**2 + (yB - yC)**2)**(1/2)  # segmento do vertice B ao C

            # funcao para encontrar o angulo do triangulo (Lei dos Cossenos)
            def calc_angulo(a, b, c):
                "retorna o angulo em graus do triangulo"
                cos_angulo = (b**2 + c**2 - a**2) / (2*b*c)
                angulo = degrees(acos(cos_angulo))
                return angulo
             
            # calculando o angulo do triangulo superior e inferior
            angulo1 = calc_angulo(a, b1, d1)
            angulo2 = calc_angulo(c, b2, d2)

            # calculo das areas de cada triangulo
            A1 = 0.5 * b1 * d1 * sin(radians(angulo1))
            A2 = 0.5 * b2 * d2 * sin(radians(angulo2))
            
            # calculando a area do terreno e adicionando ao vetor
            A = A1 + A2
            areas.append(A)
        
        # mostrando o resultado encontrado
        print('terreno A') if areas[0] > areas[1] else print('terreno B')


    def riddles_dark():  # Ok
        # input do raio
        radius = float(input())
        
        # definicao do valor de pi
        pi = 3.14
        
        # calculando a circunferencia
        circunference = 2 * pi * radius

        # mostrando o resultado formatado
        print(f'{circunference:.2f}')



Prova3.quadrado_magico()