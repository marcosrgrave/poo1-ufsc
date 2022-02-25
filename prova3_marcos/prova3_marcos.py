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


    def counting_in_chinese():
        pass


    def quadrado_magico():
        pass


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


    def matrix_ladder():  # tudo errado nessa porra
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


    def corredor():  # works, but time limit...
        # inputs iniciais
        num_salas = int(input())
        vetor = tuple(map(int, input().split()))

        # realiza a soma de todas as salas
        # e vai removendo uma por vez, da esquerda para a direita
        # registrando apenas a maior soma encontrada
        maior_soma = 0
        fim_loop = len(vetor)
        for i1 in range(fim_loop):
            soma = vetor[i1]
            for i2 in range(i1+1, fim_loop):
                if i2 - i1 > 0:
                    soma += vetor[i2]
                    if soma > maior_soma:
                        maior_soma = soma
        
        # mostrando a maior soma encontrada
        print(maior_soma)
                

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


    def battlefield():
        pass


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
        n_stickers : int = int(input())
        total_stickers : list = []
        for n in range(n_stickers):
            sticker : int = int(input())
            total_stickers.append(sticker)
        repeated = len(set(total_stickers))
        uniques  = len(total_stickers) - repeated
        print(repeated)
        print(uniques)


    def samuel_coffee_grower():  # nao cheguei na matematica
        from math import acos, degrees, sin

        for land in range(2):
            xA, yA = map(int, input().split())
            xB, yB = map(int, input().split())
            xC, yC = map(int, input().split())
            xD, yD = map(int, input().split())

            a = ((xB - xD)**2 + (yB - yD)**2)**(1/2)
            b = ((xA - xD)**2 + (yA - yD)**2)**(1/2)
            d = ((xB - xA)**2 + (yA - yB)**2)**(1/2)
            print(a)

            cos_a = (b**2 + d**2 - a**2) / (2*b*d)
            print(cos_a)
            print(angulo := degrees(acos(cos_a)))

            print(d*b*sin(angulo)/2)


    def riddles_dark():  # Ok
        # input do raio
        radius = float(input())
        
        # definicao do valor de pi
        pi = 3.14
        
        # calculando a circunferencia
        circunference = 2 * pi * radius

        # mostrando o resultado formatado
        print(f'{circunference:.2f}')



Prova3.repeated_stickers()