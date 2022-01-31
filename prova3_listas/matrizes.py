# Obs: para usar o arquivo inputs3.txt como inputs da funcao a ser testada, basta digitar no terminal:
# python3 {arquivo_funcoes.py} < {arquivo_inputs.txt}

# MATRIZES - LISTA 1

def line_in_array():  # Ok
    # sao 144 inputs, referentes a uma matrix 12x12, onde cada input é uma célula (Excel)
    # eu preciso pegar a linha 'line' (outro input) e fazer uma 'operacao' com os numeros daquela linha

    # linha 2: começa no value 25 (12 da linha 0 + 12 da linha 1) e termina no 25+11 = 36
    # start = line_input*12 + 1
    # end = start + 11


    line_input : int = int(input())
    operation : str = input()

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


def below_the_main_diagonal():
    pass


def above_secundary_diagonal():
    pass


def below_secundary_diagonal():
    pass


def top_area():
    pass


def square_matrix_1():
    pass


def contest():
    pass


def binos_challenge():
    pass



# MATRIZES - LISTA 2

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



line_in_array()
