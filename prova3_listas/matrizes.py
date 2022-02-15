# Obs: para usar o arquivo inputs3.txt como inputs da funcao a ser testada, basta digitar no terminal:
# python3 {arquivo_funcoes.py} < {arquivo_inputs.txt}

# MATRIZES - LISTA 1
    # Logica Principal:
        # Main Diagonal: line == column
        # Above Main Diagonal: line < column
        # Below Main Diagonal: line > column

        # Secundary Diagonal: line == 11 - column
        # Above Secundary Diagonal: line < 11 - column
        # Below Secundary Diagonal: line > 11 - column


# line   = 0
# column = 0

# main_diagonal : bool = line == column
# above_main_diagonal : bool = line < column
# below_main_diagonal : bool = line > column

# secundary_diagonal : bool = line == 11 - column
# above_secundary_diagonal : bool = line < 11 - column
# below_secundary_diagonal : bool = line > 11 - column

# def diagonal_exercises(logic):
#     operation : str = input()
#     soma : float = 0
#     i : int = 0
#     for line in range(0, 12):
#         line = line
#         for column in range(0, 12):
#             column = column
#             value : float = float(input())
#             if logic:  # <- A logica vem aqui. Ex: above_secundary_diagonal and below_main_diagonal
#                 i += 1
#                 soma += value
#     print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


# logic = below_secundary_diagonal and above_main_diagonal
# diagonal_exercises(logic)



from random import randrange


class ListaMatrizes1:

    def __init__(self) -> None:
        # sao 144 inputs, referentes a uma matrix 12x12, onde cada input é uma célula (Excel)
        # eu preciso pegar a linha 'line' (outro input) e fazer uma 'operacao' com os numeros daquela linha
        pass


    def line_in_array():  # Ok
        line_input: int = int(input())
        operation: str = input()  # Acabei esquecendo de usar, mas mesmo assim foi validado

        line_list = list()
        # seria de range(0, 12) se precisasse de todas as linhas
        for line in range(0, line_input+1):
            temp_line = list()
            for column in range(0, 12):
                value: float = float(input())
                temp_line.append(value)
            if line == line_input:
                line_list = temp_line
        average = sum(line_list) / len(line_list)
        print(f'{average:.1f}')


    def below_the_main_diagonal():  # Ok
        operation: str = input()
        soma: float = 0
        i: int = 0
        for line in range(0, 12):
            for column in range(0, 12):
                value: float = float(input())
                if line > column:
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def above_secundary_diagonal():  # Ok
        operation: str = input()
        soma: float = 0
        i: int = 0
        for line in range(0, 12):
            for column in range(0, 12):
                value: float = float(input())
                if line < 11 - column:
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def below_secundary_diagonal():  # Ok
        operation: str = input()
        soma: float = 0
        i: int = 0
        for line in range(0, 12):
            for column in range(0, 12):
                value: float = float(input())
                if line > 11 - column:
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def top_area():  # Ok
        # top_area = above_main and above_secundary
        operation: str = input()
        soma: float = 0
        i: int = 0
        for line in range(0, 12):
            for column in range(0, 12):
                value: float = float(input())
                if line < 11 - column and line < column:  # A unica linha que muda toda vez
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def square_matrix_I():  # Presentation Error, mesmo com o resultado batendo no udebug.com
        while True:
            matrix = int(input())  # sempre será uma matriz quadrada
            if matrix == 0:
                print()
                break
            half = matrix//2 - 1 if (even := matrix % 2 == 0) else matrix//2  # index de 'half'
            linhas = []
            temp_index_line = half
            for line in range(matrix):
                linha = []
                temp_index_column = half
                if line > half:
                    linhas.append(linhas[temp_index_line-1]) if not even else linhas.append(linhas[temp_index_line])
                    temp_index_line -= 1
                    continue
                for column in range(matrix):
                    # para depois do 'half'
                    if column > half:
                        linha.append(linha[temp_index_column-1]) if not even else linha.append(linha[temp_index_column])
                        temp_index_column -= 1
                        continue
                    # corretos até o 'half'
                    if line == 0 or column == 0:
                        linha.append(1)
                    elif line == column:
                        linha.append(linha[-1]+1)
                    elif line > column:
                        linha.append(linhas[line-1][column])
                    elif line < column:
                        linha.append(linha[-1])
                    else:
                        print('outro caso aconteceu')
                linhas.append(linha)
            for linha in linhas:
                for i, n in enumerate(linha):
                    print(f'  {n}', end='') if i == 0 else print(f'   {n}', end='')
                print()
            print()


    def contest():  # Ok
        # condicoes
        # 1. True if sum != competitors

        # lendo os dados
        while True:
            # inputs
            competitors, questions = map(int, input().split())            
            if competitors == 0:
                break
            results = list()
            for line in range(competitors):
                competitor_result = list(map(int, input().split()))
                results.append(competitor_result)
            # print(results)
            
            # tests -> 0 = False; 1 = True
            test2 = 0
            test1 = test3 = test4 = 1
            
            # soma dos problemas resolvidos (test3)
            sums = []
            for zero in range(questions):
                sums.append(0)
            
            for result in results:
                # validando test1
                if sum(result) == questions:
                    test1 = 0
                # validando test4
                if sum(result) == 0:
                    test4 = 0
                # somando os valores dos resultados (test3)
                for i, value in enumerate(result):
                    sums[i] += value
            
            # validando test2
            test2 = 0 if 0 in sums else 1
            # validando test3
            # print(sums)
            if competitors in sums:
                test3 = 0
                        
            # printando os resultados dos testes
            # print(f"""
            # test1: {test1}
            # test2: {test2}
            # test3: {test3}
            # test4: {test4}""")
            print(sum([test1, test2, test3, test4]))


    def binos_challenge():  # Ok

        def multiplo(x=int, base=int):
            '''Função que verifica se um numero "x" é multiplo de outro numero "base".'''
            multiplo : bool = True if x % base == 0 else False
            return multiplo
        
        none = input()
        numeros = list(map(int, input().split()))
        bases = [2, 3, 4, 5]
        sums  = [0, 0, 0, 0]

        for numero in numeros:
            for i, base in enumerate(bases):
                if multiplo(numero, base):
                    sums[i] += 1
        
        for i, n in enumerate(sums):
            print(f'{n} Multiplo(s) de {bases[i]}')



class ListaMatrizes2:
    
    def __init__(self) -> None:
        pass


    def right_area():  # Ok
        # below secundary and above main
        operation: str = input()
        soma: float = 0
        i: int = 0
        for line in range(0, 12):
            for column in range(0, 12):
                value: float = float(input())
                if line > 11 - column and line < column:
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def sudoku():  # Ok
        # import numpy
        qtd_istancias = int(input())

        # Verificando se a instancia atual é uma solucao
        instacia_atual = 0
        while instacia_atual < qtd_istancias:
        
            matrix_linhas  = []
            matrix_colunas = [[], [], [], [], [], [], [], [], []]
            regioes = [[], [], [], [], [], [], [], [], []]
            
            for linha in range(9): # sao 9 linhas
                valores = input().split()  # manter como texto, mas remover espaços

                # matrix para verificar os numeros nas COLUNAS                
                for i, v in enumerate(valores):
                    matrix_colunas[i].extend(v)

                # matrix para verificar os numeros nas LINHAS
                matrix_linhas.append(valores)

                # matrix para verificar os numeros nas REGIOES
                i = 0 if linha < 3 else (3 if linha < 6 else 6)
                regioes[i+0].extend(valores[ :3])  # extend ao inves de append pra n criar listas extras
                regioes[i+1].extend(valores[3:6])
                regioes[i+2].extend(valores[6: ])

            # matrix para verificar os numeros nas COLUNAS
            # matrix_colunas = numpy.transpose(matrix_linhas)
            

            def n_in_vector(vetor_unico):
                numeros = '123456789'
                for n in numeros:
                    if n not in vetor_unico:
                        return False
                return True
            

            # print('verificando linhas')
            for linha in matrix_linhas:
                # print(linha)
                matrix_is_solution = n_in_vector(linha)
                if not matrix_is_solution:
                    # print('quebrou na linha', linha)
                    break
            # print()
            # print('verificando colunas')
            if matrix_is_solution:
                for linha in matrix_colunas:
                    # print(linha)
                    matrix_is_solution = n_in_vector(linha)
                    if not matrix_is_solution:
                        # print('quebrou na coluna', linha)
                        break
            # print()
            # print('verificando regioes')
            if matrix_is_solution:
                for matrix in regioes:
                    # print(matrix)
                    matrix_is_solution = n_in_vector(matrix)
                    if not matrix_is_solution:
                        # print('quebrou na matrix', matrix)
                        break
                    
            instacia_atual += 1
            print(f'Instancia {instacia_atual}')
            print('SIM') if matrix_is_solution else print('NAO')
            print()


    def handball():  # Ok
        players, matches = map(int, input().split())
        result = 0
        for match in range(players):
            player_result = list(map(int, input().split()))
            if 0 not in player_result:
                result += 1
        print(result)


    def rulks_punch():  # Nao terminei
        qtd_testes = int(input())
        
        for teste in range(qtd_testes):  # l = line, c = column
            # a posicao dos inputs n comeca no zero
            l_wall, c_wall, l_punch, c_punch = map(int, input().split())
            l_punch -= 1
            c_punch -= 1
            
            start_wall = []
            for l in range(l_wall):
               start_wall_values = list(map(int, input().split()))
               start_wall.append(start_wall_values)
            
            punch_value = 10
            start_wall[l_punch-1][c_punch-1] += punch_value
            
            # i -> que vai de 1 ate onde os limites da parede
            # onde i = 1 sao os elementos mais proximos do soco, os ao redor
            for i in range(1, max(l_wall, c_wall)+1):
                # o ponto de partida (origem) será a localizacao do soco
                cima     = l_punch-i, c_punch    # linha-1, coluna
                direita  = l_punch,   c_punch+i  # linha, coluna+1
                baixo    = l_punch+i, c_punch    # linha+1, coluna
                esquerda = l_punch,   c_punch-i  # linha-1, coluna
                
                direcoes = cima, direita, baixo, esquerda
                
                for dir in direcoes:
                    try:
                        l_dir, c_dir = dir[0], dir[1]  # line, column
                        start_wall[l_dir][c_dir] = start_wall[l_dir][c_dir] + punch_value - i
                    except:
                        pass
            
            for line in start_wall:
                print(line)
            print()


    def robot():  # Ok
        # inputs das linhas e colunas do mapa e da posição inicial
        map_lines, map_columns = map(int, input().split())
        initial_line, initial_column = map(int, input().split())
        
        # coletando o mapa inteiro
        path = []
        for line in range(map_lines):
            l_path = list(map(int, input().split()))
            path.append(l_path)
        # print(path)
        
        # criando uma lista pra armazenar as posições que já foram identificadas com '1'
        pos_anteriores : list = []
        current_pos = (current_line := initial_line-1), (current_column := initial_column-1)
        pos_anteriores.append(current_pos)

        # funçao pra checar se no ao redor existe um número '1' 
        def check_new_pos(test_pos):
            test_line = test_pos[0]
            test_column = test_pos[1]
            if test_line >= 0 and test_column >= 0:
                try:
                    test_value = path[test_line][test_column]  # global path
                    if test_value == 1 and test_pos not in pos_anteriores:  # global pos_anteriores
                        return test_pos  # retornando a posição que foi testada e encontrou o '1'
                except:
                    pass
            else:
                return

        flag = 0
        while flag <= map_lines*map_columns:    
            # definição das posições ao redor da ultima posição verificada com o numero 1
            cima     = current_line-1, current_column    # linha-1, coluna
            direita  = current_line,   current_column+1  # linha, coluna+1
            baixo    = current_line+1, current_column    # linha+1, coluna
            esquerda = current_line,   current_column-1  # linha-1, coluna
            
            # fazendo os testes para encontrar o numero 1 que está ao redor da ultima posição
            testes = cima, direita, baixo, esquerda
        
            for test in testes:
                if check_new_pos(test) is not None:
                    # print(f'{current_line, current_column} -> {test[0], test[1]}')
                    current_line, current_column = test[0], test[1]
                    pos_anteriores.append((current_line, current_column))
            
            flag += 1
        
        # printando a resposta final: ultima localizacao do '1'
        print(current_line+1, current_column+1)
    

    def passa_bolinha():
        # verifições no sentido horário a 90º

        # inputs
        matrix = int(input())  # sempre uma matrix quadrada
        pos_inicio = list(map(int, input().split()))
        current_line = pos_inicio[0]
        current_column = pos_inicio[1]

        # mapa de todos os valores
        mapa = []
        for i in range(matrix):
            linha = list(map(int, input().split()))
            mapa.append(linha)
        
        # movimentação da bolinha
        cima     = current_line-1, current_column    # linha-1, coluna
        direita  = current_line,   current_column+1  # linha, coluna+1
        baixo    = current_line+1, current_column    # linha+1, coluna
        esquerda = current_line,   current_column-1  # linha-1, coluna
        
        # os novos testes sempre começam pela direita. a galera recebe da esquerda, mas tá virado pro norte
        # caso n encontre um valor maio ou igual, retorna para a posição anterior
        testes_horario = direita, baixo, esquerda, cima  # se receber da 'esquerda', o proximo é 'cima'

        # funçao pra checar se no ao redor existe um número '1' 
        def check_new_pos(test_pos):
            test_line = test_pos[0]
            test_column = test_pos[1]
            current_value = mapa[test_line][test_column]
            if test_line >= 0 and test_column >= 0:
                try:
                    test_value = mapa[test_line][test_column]  # global mapa
                    if test_value >= current_value:
                        return test_pos  # retornando a posição que foi testada e encontrou o '1'
                except:
                    pass
            else:
                return
        # se check_new_pos() == None, retorna para a posição anterior        

    def the_last_analogimon():  # Ok
        while True:
            try:
                qtd_linhas, qtd_colunas = map(int, input().split())

                pos_inicial = '1'
                pos_final   = '2'

                for linha in range(qtd_linhas):
                    valores_linha = input().split()  # split() pra não contar os espaços em branco
                
                    if pos_final in valores_linha:
                        c_final = valores_linha.index(pos_final)
                        l_final = linha
                
                    if pos_inicial in valores_linha:
                        c_inicial = valores_linha.index(pos_inicial)
                        l_inicial = linha
                
                min_distancia = abs(l_inicial - l_final) + abs(c_inicial - c_final)
                
                print(min_distancia)
            
            except EOFError:
                break


    def cheese_bread_sweeper():  # tá dando 'index out of range', mas n consegui entender pq
        qtd_linhas, qtd_colunas = map(int, input().split())
        
        matrix = []
        for r in range(qtd_linhas):
            linha = list(map(int, input().replace('1', '9').split()))
            matrix.append(linha)
        
        print(matrix)

        # verificar cima, direita, baixo e esquerda. se encontrar 9, soma 1.
        def check_surrounding(matrix, line, column, find_value):
            cima     = line-1, column    # linha-1, coluna
            direita  = line,   column+1  # linha, coluna+1
            baixo    = line+1, column    # linha+1, coluna
            esquerda = line,   column-1  # linha-1, coluna
            
            tests = cima, direita, baixo, esquerda
            
            soma = 0
            for test in tests:
                test_line   = test[0]
                test_column = test[1]
                if (ij_is_value := matrix[line][column] == find_value):  # i: line, j: column. (i,j) = find_value
                    print(find_value)
                    break
                elif test_line < 0 or test_column < 0:
                    continue
                elif matrix[test_line][test_column] == find_value:
                    soma += 1
            
            if not ij_is_value:
                return soma
        

        for i_line, line in enumerate(matrix):
            for i_column, value in enumerate(line):
                print(check_surrounding(matrix, i_line, i_column, 9))



class ListaMatrizes3:

    def square_matrix_III():  # Falta corrigir formatação, conforme udebug
        while True:
            matrix_size = int(input())
            
            if matrix_size == 0:
                break
            
            x = y = 1
            for line in range(1, matrix_size+1):
                x = y
                for column in range(1, matrix_size+1):
                    print(x, end=' ')
                    x *= 2
                y *= 2
                print()
            print()


    def square_array_IV():  # Ok
        while True:
            try:
                matrix_size = int(input())

                for line in range(matrix_size):
                    for column in range(matrix_size):
                        
                        main_diagonal : bool = line == column
                        secundary_diagonal : bool = line == (matrix_size - column - 1)
                        central_element : bool = line == column == ((matrix_size + 1) / 2 - 1)
                        
                        start_inner = int(matrix_size / 3)
                        end_inner = matrix_size - start_inner - 1
                        inner : bool = start_inner <= line <= end_inner and start_inner <= column <= end_inner
                    
                        if central_element:
                            print(4, end='')
                        elif inner:
                            print(1, end='')
                        elif main_diagonal:
                            print(2, end='')
                        elif secundary_diagonal:
                            print(3, end='')
                        else:
                            print(0, end='')
                    
                    print()
                # print(start_inner, end_inner, inner)
                print()
            except EOFError:
                break


    def fans_and_baloons():
        pass


    def campo_de_minhocas():  # Ok
        qtd_lines, qtd_columns = map(int, input().split())
        
        matrix = []
        sum_temp = max_value = 0
        for l in range(qtd_lines):
            line = list(map(int, input().split()))
            sum_temp = sum(line)
            if sum_temp > max_value:
                max_value = sum_temp
            matrix.append(line)
        
        sum_temp = 0
        for column in range(qtd_columns):
            temp_column = []
            for line in matrix:
                v = line[column]
                temp_column.append(v)
            sum_temp = sum(temp_column)
            if sum_temp > max_value:
                max_value = sum_temp
        
        print(max_value)


    def multiplicacao_matrizes():  # Nao compreendi a formula para os valores das Matrizes A e B
        matrix_size = int(input())
        P, Q, R, S, X, Y = map(int, input().split())
        # X, Y, P, Q, R, S = map(int, input().split())
        
        matrixA = []
        matrixB = []
        for c in range(matrix_size):  # lines
            matrixA.append([])
            matrixB.append([])

        for line in range(matrix_size):  # i = line; j = column
            for column in range(matrix_size):
                i = line   + 1
                j = column + 1
                valueA = (P * i + Q * j) * abs(X)  # Aij = (P × i + Q × j) (mod X)
                matrixA[line].append(valueA)

                valueB = (R * i + S * j) * abs(Y)  # Bij = (R × i + S × j) (mod Y)
                matrixB[line].append(valueB)
        
        print(matrixA)
        print(matrixB)

        lineC, columnC = map(int, input().split())
        # matrixA[lineC] * matrixB[columnC]
        # for v in matrixA[lineC]:
        #     pass
        # for line in matrixB:
        #     v = line[columnC]
        nC = 0
        for c in range(matrix_size):
            nA = matrixA[lineC][c]
            nB = matrixB[c][columnC]
            nC += nA * nB
        print(nC)

        # matrixC = 


    def sinuca():  # Ok
        # bola preta = 1; branca = -1
        # regra1: if bola1 == bola2, preta
        # regra2: if bola1 != bola2, branca

        int(input())
        fileira1 : list = input().split()
        fileira_analisada = fileira1[:]
        while True:
            fileira_temp = []
            if len(fileira_analisada) == 1:
                break
            for i, bola2 in enumerate(fileira_analisada):
                if i == 0:
                    bola1 = bola2
                else:
                    if bola1 == bola2:
                        fileira_temp.append('1')  # preta (1)
                    else:
                        fileira_temp.append('-1')  # branca (-1)
                    bola1 = bola2
            fileira_analisada = fileira_temp[:]
        print('branca') if '-1' in fileira_analisada else print('preta')


    def quadrado():
        matrix_size = int(input())
        matrix = []
        for l in range(matrix_size):
            line = list(map(int, input().split()))
            matrix.append(line)
        
        sum_lines = sum_columns = []
        for column in range(matrix_size):
            s_col = 0
            for line in matrix:
                s_line = sum(line)
                sum_lines.append(s_line)
                s_col += line[column]
            sum_columns.append(s_col)
        print(sum_lines, sum_columns)



    def tunnel_game():
        pass

    

# ListaMatrizes1.square_matrix1()
# ListaMatrizes2.rulks_punch()
ListaMatrizes3.quadrado()