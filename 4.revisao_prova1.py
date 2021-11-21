
def quadrant():
    respostas = []
    while True:
        entry = input().split()
        X = int(entry[0])
        Y = int(entry[1])
        if X == 0 or Y == 0:
            break
        if X>0 and Y>0:
            respostas.append('primeiro')
        elif X<0 and Y>0:
            respostas.append('segundo')
        elif X<0 and Y<0:
            respostas.append('terceiro')
        else:
            respostas.append('quarto')

    for resposta in respostas:
        print(resposta)


def what_is_the_fastest():
    times = list(map(float, input().split()))  # time in seconds
    competitors = ['Otavio', 'Bruno', 'Ian']
    podium = sorted(times)  # winner has the lowest time
    if podium[0] == podium[1]:
        print('Empate')
    else:
        print(competitors[times.index(podium[0])])


def capuchin_monkey():
    resps = []
    i = 1
    while True:
        qtd_retangulos = int(input())
        if qtd_retangulos == 0:
            break
        
        # Pegando os pontos dos retangulos
        listx1 = list()
        listx2 = list()
        listy1 = list()
        listy2 = list()
        for retangulo in range(0, qtd_retangulos):
            entry = input().strip().split()
            X1, Y1, X2, Y2 = int(entry[0]), int(entry[1]), int(entry[2]), int(entry[3])

            # pts_temp = []
            # for n in range(X1, X2+1):
            #     pts_temp.append(n)
            # ptsX.append(pts_temp[:])
            
            # pts_temp.clear()
            # for n in range(Y2, Y1+1):
            #     pts_temp.append(n)
            # ptsY.append(pts_temp[:])

            listx1.append(X1)
            listx2.append(X2)
            listy1.append(Y1)
            listy2.append(Y2)

        # Filtrando os pontos em comum
        comum_x = [max(listx1), min(listx2)]  # esse tipo de filtro não indica se existem pontos em comum
        comum_y = [min(listy1), max(listy2)]

        resps.append(f'Teste {i}\n{comum_x[0]} {comum_y[0]} {comum_x[1]} {comum_y[1]}\n')
        i += 1

    for r in resps:
        print(r)

def bafo():
    resps = list()
    c = 1
    while True:
        rodadas = int(input())
        if rodadas == 0:
            break
        
        sumA = sumB = 0
        for i in range(0, rodadas):
            pts = list(map(int, input().strip().split()))
            sumA += pts[0]
            sumB += pts[1]
        winner = 'Aldo' if sumA > sumB else 'Beto'
        resps.append(f'Teste {c}\n{winner}\n')
        c += 1
    
    for r in resps:
        print(r)


def easy_diff_btwn_dates():
    from datetime import date
    entryA = input().strip().split()
    entryB = input().strip().split()
    dateA = date(2021, int(entryA[1]), int(entryA[0]))
    dateB = date(2021, int(entryB[1]), int(entryB[0]))
    dif = dateB - dateA
    print(dif.days)


def elevator():
    elevator_data = list(map(int, input().strip().split()))
    sensor_readings, max_capacity = elevator_data[0], elevator_data[1]
    
    exccess = False
    elevator_occupancy = 0
    for i in range(0, sensor_readings):
        movement = list(map(int, input().strip().split()))
        came_out, came_in = movement[0], movement[1]
        elevator_occupancy += came_in - came_out
        if elevator_occupancy > max_capacity:
            exccess = True

    print('S') if exccess else print('N')


def escada_rolante():
    number_people = int(input())
    delay = 10  # seconds

    person_data = list()
    for i in range(0, number_people):
        person_data.append(int(input()))
        if i == 0:
            total_time = 0
        elif (dif:= person_data[i] - person_data[i-1]) <= delay:
            total_time += dif
            
        if i == number_people-1:
            total_time += delay
    print(total_time)


def album_fotos():
    dimensao_pag = input().strip().split()
    dimensao_foto1 = input().strip().split()
    dimensao_foto2 = input().strip().split()
    larg_pag, alt_pag = int(dimensao_pag[0]), int(dimensao_pag[1])
    larg_foto1, alt_foto1 = int(dimensao_foto1[0]), int(dimensao_foto1[1])
    larg_foto2, alt_foto2 = int(dimensao_foto2[0]), int(dimensao_foto2[1])

    fit = False
    # Caso 1: As duas na Horizontal
    if larg_pag >= larg_foto1 and larg_pag >= larg_foto2:# or alt_pag > alt_foto1 and alt_pag > alt_foto2:
        if alt_pag >= alt_foto1 + alt_foto2:# or larg_pag > larg_foto1 + larg_foto2:
            fit = True

    # Caso 2: As duas na Vertical
    if alt_pag >= alt_foto1 and alt_pag >= alt_foto2:
        if larg_pag >= larg_foto1 + larg_foto2:
            fit = True

    # Caso 3: Uma na Horizontal, a outra na Vertical
    cenario1 = alt_pag >= alt_foto1 + larg_foto2 and larg_pag >= larg_foto1 + alt_foto2
    cenario2 = larg_pag >= larg_foto1 + alt_foto2 and alt_pag >= alt_foto1 + larg_foto2
    if cenario1 or cenario2:
        fit = True 

    print('S') if fit else print('N')


def chocolate():
    largura_barra = int(input())  # a barra é quadrada
    pedacos = 1
    while largura_barra >= 2:
        pedacos = pedacos * 4
        largura_barra = largura_barra / 2
    print(pedacos)
    
    # Método que não funcionou: (nao consegui testar valores para entender em qual momento ele n serve)
    # largura_barra = int(input())
    # if largura_barra >= 2:
    #     print(largura_barra**2) if largura_barra % 2 == 0 else print((largura_barra-1)**2)


def saldo_do_vovo():
    entry = input().strip().split()
    total_periodos = int(entry[0])
    saldo_conta = int(entry[1])

    saldos_periodo = list()
    for periodo in range(0, total_periodos):
        movimentacao_periodo = int(input())
        saldo_conta += movimentacao_periodo
        saldos_periodo.append(saldo_conta)
    print(min(saldos_periodo))


def old_clock():
    while True:
        try:
            entry = input().strip().split()
            h_angle = int(entry[0])
            m_angle = int(entry[1])
            # h_angle, m_angle = map(int, input().strip().split())  # a funcao map() torna o codigo bem mais lento

            h = h_angle/360 * 12  # 360º = 12 hours
            m = m_angle/360 * 60  # 360º = 60 minutes

            time = f'{int(h):02d}:{int(m):02d}'
            print(time)

        except EOFError:
            break


def kikoho():
    test_cases = int(input())
    for test_case in range(0, test_cases):        
        entry = input().strip().split()
        X1, Y1, X2, Y2, X3, Y3 = int(entry[0]), int(entry[1]), int(entry[2]), int(entry[3]), int(entry[4]), int(entry[5])
        
        # METODO DA DIFERENÇA DAS ÁREAS: (DÁ ERRO EM ALGUNS CASOS)
        # segmX = list()
        # segmY = list()
        # area_triangulos = list()

        # segmX.append(abs(X1 - X2))
        # segmX.append(abs(X1 - X3))
        # segmX.append(abs(X2 - X3))

        # segmY.append(abs(Y1 - Y2))
        # segmY.append(abs(Y1 - Y3))
        # segmY.append(abs(Y2 - Y3))

        # for i in range(0, 3):
        #     areax = segmX[i] * segmY[i] / 2
        #     area_triangulos.append(areax)
        # area_quadrado = max(segmX) * max(segmY)
        
        # area_resp = area_quadrado - sum(area_triangulos)

        # METODO DO DETERMINANTE:
        D = ((X1*Y2 + Y1*X3 + X2*Y3) - (X3*Y2 + X2*Y1 + Y3*X1)) / 2
        area_resp = abs(D)

        print(f'{area_resp:.3f}')

capuchin_monkey()
