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


    def square_matrix1():  # Presentation Error, mesmo com o resultado batendo no udebug.com
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


    def sudoku():
        pass


    def handball():  # Ok
        players, matches = map(int, input().split())
        result = 0
        for match in range(players):
            player_result = list(map(int, input().split()))
            if 0 not in player_result:
                result += 1
        print(result)


    def rulks_punch():
        pass


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


    def the_last_analogimon():
        pass


    def cheese_bread_sweeper():
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
                


# ListaMatrizes1.square_matrix1()
ListaMatrizes2.cheese_bread_sweeper()