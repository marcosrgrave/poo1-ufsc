def average1():
    pass


def average2():
    A = float(input())
    B = float(input())
    C = float(input())

    avg = (A * 2.0 + B * 3.0 + C * 5.0) / (2.0 + 3.0 + 5.0)
    print(f'MEDIA = {avg:.1f}')


def difference():
    A = int(input('A: '))
    B = int(input('B: '))
    C = int(input('C: '))
    D = int(input('D: '))

    dif = A * B - C * D
    print(f'DIFERENCA = {dif}')


def salary():
    id = 25  # int(input())
    worked_hours = 100  # int(input())
    amount_per_hour = 5.5  # float(input())

    print(f'NUMBER = {id}\nSALARY = U$ {amount_per_hour * worked_hours:.2f}')


def sallary_with_bonus():
    name = 'JOAO'  # input()
    fixed_salary = 500.00  # float(input())
    total_sales = 1230.30  # float(input())
    commission = 0.15

    final_salary = fixed_salary + total_sales * (commission)
    print(f'TOTAL = R$ {final_salary:.2f}')


def area():
    entry = input().strip().split()
    A = float(entry[0])
    B = float(entry[1])
    C = float(entry[2])

    pi = 3.14159

    triang_area = A * C / 2
    circ_area = pi * C ** 2
    trap_area = (A + B) * C / 2
    square_area = B ** 2
    rect_area = A * B
    print(
        f'TRIANGULO: {triang_area:.3f}\nCIRCULO: {circ_area:.3f}\nTRAPEZIO: {trap_area:.3f}\nQUADRADO: {square_area:.3f}\nRETANGULO: {rect_area:.3f}')


def consumption():
    total_distance = int(input())
    spent_fuel = float(input())

    avg_consumption = total_distance / spent_fuel
    print(f'{avg_consumption:.3f} km/l')


def distance_between_two_points():
    entry1 = input().strip().split()
    entry2 = input().strip().split()
    x1 = float(entry1[0])
    y1 = float(entry1[1])
    x2 = float(entry2[0])
    y2 = float(entry2[1])

    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    print(f'{dist:.4f}')


def fuel_spent():
    CONSUMPTION = 12  # km/l
    spent_time = 10  # hours
    avg_speed = 85  # km/h

    # CONSUMPTION = 12  # km/l
    # spent_time = int(input())
    # avg_speed = int(input())

    fuel_needed = avg_speed * spent_time / CONSUMPTION
    print(f'{fuel_needed:.3f}')


def time_conversion():
    duration = 140153

    # duration = int(input())

    hours = duration // (60 * 60)  # 1 h = 60 min = 60 sec // 1h = 60*60 sec
    minutes = (duration - hours * 60 * 60) // 60
    seconds = duration - hours * 60 * 60 - minutes * 60

    print(f'{hours}:{minutes}:{seconds}')


def age_in_days():
    age_in_days = 400  # in days

    # age_in_days = int(input())
    YEAR = 365  # days
    MONTH = 30  # days per month

    years = age_in_days // YEAR
    months = (age_in_days - years * YEAR) // MONTH
    days = age_in_days - months * MONTH - years * YEAR

    print(f'{years} ano(s)\n{months} mes(es)\n{days} dia(s)')


def regular_simple_polygons():
    entry = input().strip().split()
    number_sides = int(entry[0])
    length_sides = int(entry[1])

    if number_sides > 0 and length_sides > 0 and 3 <= number_sides and number_sides <= 1000000 and 1 <= length_sides and length_sides <= 4000:
        perimeter = number_sides * length_sides
        print(perimeter)


def pneu():
    pressao_desejada = int(input())  # 1 ≤ N ≤ 40
    pressao_lida = int(input())  # 1 ≤ M ≤ 40
    dif = pressao_desejada - pressao_lida
    print(dif)


def transporte_containers():
    entry1 = input().strip().split()
    larg_container = int(entry1[0])
    compr_container = int(entry1[1])
    alt_container = int(entry1[2])

    entry2 = input().strip().split()
    larg_navio = int(entry2[0])
    compr_navio = int(entry2[1])
    alt_limite_navio = int(entry2[2])

    qtd_larg = larg_navio // larg_container
    qtd_compr = compr_navio // compr_container
    qtd_alt = alt_limite_navio // alt_container

    print(qtd_larg * qtd_compr * qtd_alt)


def busca_internet():
    link3 = int(input())
    link2 = 2 * link3
    link1 = 2 * link2
    print(link1)
