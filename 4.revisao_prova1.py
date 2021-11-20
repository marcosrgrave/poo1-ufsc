
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
    pass


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
    pass


def chocolate():
    L = int(input())  # lado em cm
    if L >= 2:
        print(L**2) if L % 2 == 0 else print((L-1)**2)
    else:
        print(1)


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
    pass


def kikoho():
    resps = list()
    
    test_cases = int(input())
    for test_case in range(0, test_cases):
        segmX = list()
        segmY = list()
        area_triangulos = list()
        
        entry = input().strip().split()
        X1, Y1, X2, Y2, X3, Y3 = int(entry[0]), int(entry[1]), int(entry[2]), int(entry[3]), int(entry[4]), int(entry[5])
        
        segmX.append(abs(X1 - X2))
        segmX.append(abs(X1 - X3))
        segmX.append(abs(X2 - X3))

        segmY.append(abs(Y1 - Y2))
        segmY.append(abs(Y1 - Y3))
        segmY.append(abs(Y2 - Y3))

        for i in range(0, 3):
            areax = segmX[i] * segmY[i] / 2
            area_triangulos.append(areax)
        area_quadrado = max(segmX) * max(segmY)
        
        areaX = area_quadrado - sum(area_triangulos)
        resps.append(areaX)
    
    for r in resps:
        print(f'{r:.3f}')


kikoho()
