# Obs: para usar o arquivo inputs3.txt como inputs da funcao a ser testada, basta digitar no terminal:
# python3 {arquivo_funcoes.py} < {arquivo_inputs.txt}

# MATRIZES - LISTA 1
    ## Logica Principal:
        ### Main Diagonal: line == column
        ### Above Main Diagonal: line < column
        ### Below Main Diagonal: line > column

        ### Secundary Diagonal: line == 11 - column
        ### Above Secundary Diagonal: line < 11 - column
        ### Below Secundary Diagonal: line > 11 - column

class ListaMatrizes1:

    def __init__(self) -> None:
        # sao 144 inputs, referentes a uma matrix 12x12, onde cada input é uma célula (Excel)
        # eu preciso pegar a linha 'line' (outro input) e fazer uma 'operacao' com os numeros daquela linha
        pass


    def line_in_array():  # Ok
        line_input : int = int(input())
        operation : str = input()  # Acabei esquecendo de usar, mas mesmo assim foi validado

        line_list = list()
        for line in range(0, line_input+1):  # seria de range(0, 12) se precisasse de todas as linhas 
            temp_line = list()
            for column in range(0, 12):
                value : float = float(input())
                temp_line.append(value)
            if line == line_input:
                line_list = temp_line
        average = sum(line_list) / len(line_list)
        print(f'{average:.1f}')


    def below_the_main_diagonal():  # Ok
        operation : str = input()
        soma : float = 0
        i : int = 0
        for line in range(0, 12):
            for column in range(0, 12):
                value : float = float(input())
                if line > column:
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def above_secundary_diagonal():  # Ok
        operation : str = input()
        soma : float = 0
        i : int = 0
        for line in range(0, 12):
            for column in range(0, 12):
                value : float = float(input())
                if line < 11 - column:
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def below_secundary_diagonal():  # Ok
        operation : str = input()
        soma : float = 0
        i : int = 0
        for line in range(0, 12):
            for column in range(0, 12):
                value : float = float(input())
                if line > 11 - column:
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def top_area():  # Ok
        # top_area = above_main and above_secundary
        operation : str = input()
        soma : float = 0
        i : int = 0
        for line in range(0, 12):
            for column in range(0, 12):
                value : float = float(input())
                if line < 11 - column and line < column:  # A unica linha que muda toda vez
                    i += 1
                    soma += value
        print(f'{soma:.1f}') if operation in 'sS' else print(f'{soma/i:.1f}')


    def square_matrix1():
        pass


    def contest():
        results = list()
        competitors, questions = map(int, input().split())
        for line in range(competitors):
            competitor_result = list(map(int, input().split()))
            results.append(competitor_result)
        print(results)


    def binos_challenge():
        pass


class ListaMatrizes2:
    
    def __init__(self) -> None:
        pass


    def XXXXX():
        pass


    def XXXXX():
        pass


    def XXXXX():
        pass


    def XXXXX():
        pass


    def XXXXX():
        pass


    def XXXXX():
        pass


    def XXXXX():
        pass



ListaMatrizes1.contest()