# PARA MEDIR A PERFORMANCE DO CODIGO:
from time import perf_counter
def start_code_time():
    return perf_counter()
    
def end_code_time(start_code_time):
    end_code = perf_counter()
    time_code = end_code - start_code_time
    return time_code


def musical_loop():  # OK
    while True:
        flag = int(input())
        if flag == 0:
            break
        
        vet_list = list(map(int, input().strip().split()))
        
        peaks = 0
        for i, pt in enumerate(vet_list):
            if i != len(vet_list)-1:
                vet = [vet_list[i-1], vet_list[i], vet_list[i+1]]
            else:
                vet = [vet_list[i-1], vet_list[i], vet_list[0]]
            if vet[1] == max(vet) or vet[1] == min(vet):
                peaks += 1
        print(peaks)


def optical_reader():  # OK
    resps = []
    while True:
        total_answers = int(input())
        if total_answers == 0:
            break
        alternatives = ['A', 'B', 'C', 'D', 'E']
        
        for i in range(0, total_answers):
            answer = list(map(int, input().strip().split()))
            s = 0
            
            for i, color in enumerate(answer):
                if color <= 127:
                    alt = alternatives[i]
                    s += 1
            resps.append(alt) if s == 1 else resps.append('*')

    for r in resps:
        print(r)


def lowest_number_and_position():  # OK
    int(input())
    numbers = list(map(int, input().strip().split()))
    r = min(numbers)
    i = numbers.index(r)
 

def fake_tickets():  # OK
    while True:       
        a = input().split()
        if '0' in a:
            break
        ticket_numbers = list(map(int, input().strip().split()))
        st = set(ticket_numbers)
        s = sum_added =0
        numbers_added = []
        repeated = []
        for ticket in ticket_numbers:
            if ticket in numbers_added:
                repeated.append(ticket)
                sum_added += 1
            if ticket in st and ticket not in numbers_added:
                s += 1
                numbers_added.append(ticket)
        print(len(set(repeated)))


def head_or_tail():  # OK
    while True:
        flag = int(input())
        
        if flag == 0:
            break
        else:
            games = list(map(int, input().strip().split()))
            sum0 = sum1 = 0
            for result in games:
                if result == 0:
                    sum0 += 1
                else:
                    sum1 += 1
            
            print(f'Mary won {sum0} times and John won {sum1} times')


def sticks_game():  # OK
    '''
    sticks with variable sizes;
    draw rectangles with these sticks;
    each stick can be used in only one rectangle;
    two kids with one set of sticks each;
    wins who draw the most rectangles.
    '''

    while True:
        number_of_sets = int(input())
        if number_of_sets == 0:
            break
        two_sides = []
        for set in range(number_of_sets):
            size, amount = map(int, input().strip().split())
            two_sides.append(amount//2)
        print(sum(two_sides)//2)


def dangerous_dive():  # OK
    while True:
        try:
            went, returned = input().strip().split()
            went = int(went)  # or -> went, returned = map(int, input().strip().split())
            returned_string = input().strip().split()
            returned_list = []  # or -> returned_list = list(map(int, input().strip().split()))
            for ret in returned_string:
                ret = int(ret)
                returned_list.append(ret)
            
            went_list = []
            for i in range(1, went+1):
                went_list.append(i)
            
            not_returned_list = []
            for volunteer in went_list:
                if volunteer not in returned_list:
                    not_returned_list.append(volunteer)
            
            if not_returned_list == []:
                print('*')
            else:    
                for v in not_returned_list:
                    # print(v) if v == not_returned_list[-1] else print(v, end=' ')
                    print(v, end=' ')
                print()
            
        except EOFError:
            break


def biochemical_digital_circuit():  # OK
    while True:
        nodes, measures, min_length = map(int, input().strip().split())
        if nodes == 0 and measures == 0 and min_length == 0:
            break
        else:
            bins = []
            for m in range(0, measures):
                binary = list(map(int, input().strip().split()))
                bins.append(binary)

            answer = 0
            for i in range(nodes):  # troca na horizontal até a qtd de nodes
                s = 0
                for line in bins:  # troca na vertical
                    if line[i] == 1:
                        s += 1
                        if s == min_length:
                            answer += 1
                    else:
                        s = 0
            print(answer)


def detective_watson():  # OK
    '''
    its never the most suspicious,
    but the second most suspicious. - Sherlock Holmes
    '''
    while True:
        suspects = int(input())
        if suspects == 0:
            break
        jw_opinions = list(map(int, input().strip().split()))
        killer = sorted(jw_opinions)[-2]
        i = jw_opinions.index(killer) + 1
        print(i)


def automated_checking_machine():  # OK
    first_connector = list(map(int, input().strip().split()))
    second_connector = list(map(int, input().strip().split()))
    # 0 = outlet; 1 = plug
    not_compatible = False
    for i in range(0, 5):
        if first_connector[i] == second_connector[i]:
            not_compatible = True
            break
    print('N') if not_compatible else print('Y')


def brazilian_economy():  # OK
    citizens = int(input())
    opinions = list(map(int, input().strip().split()))
    # is_ok = 0; not_ok = 1
    not_ok = sum(opinions)
    majority = citizens // 2 + 1
    print('N') if not_ok >= majority or not_ok == citizens/2 else print('Y')


def sansas_snow_castle():  # OK
    amount_towers, necessary_peaks = map(int, input().strip().split())    
    towers = list(map(int, input().strip().split()))
    
    peaks = 0
    valleys = 0
    for i, pt in enumerate(towers):
        if i == 0 or i == len(towers)-1:
            continue        
        elif i != len(towers)-1:
            vet = [towers[i-1], towers[i], towers[i+1]]
        if vet[1] == max(vet):
            peaks += 1
        if vet[1] == min(vet):
            valleys += 1
    if peaks == necessary_peaks and valleys == peaks-1:
        print('beautiful')
    else:
        print('ugly')


def jumping_frog():  # OK
    frog_jump_height, total_pipes = map(int, input().strip().split())
    pipes_height = list(map(int, input().strip().split()))
    
    toohigh_or_toolow = False
    for i, pipe_height in enumerate(pipes_height):
        base = pipe_height if i == 0 else pipes_height[i-1]
        if abs(base - pipe_height) > frog_jump_height:
            toohigh_or_toolow = True
            break

    print('YOU WIN') if not toohigh_or_toolow else print('GAME OVER')


def airport():  # OK
    c = 0
    while True:
        airports, flights = map(int, input().strip().split())
        if airports == flights == 0:
            break
        
        arprts = []
        sums = []
        for flight in range(airports):
            arprts.append(flight+1)
            sums.append(0)

        for f in range(flights):
            airp1, airp2 = map(int, input().strip().split())
            if airp1 in arprts:
                i1 = arprts.index(airp1)
                sums[i1] += 1
            if airp2 in arprts:
                i2 = arprts.index(airp2)
                sums[i2] += 1

        maxim = max(sums)
        indexs = []
        for i, v in enumerate(sums):
            if v == maxim:
                indexs.append(i)

        # Printando os resultados
        c += 1
        print(f'Teste {c}')
        for i in range(len(indexs)):
            print(arprts[indexs[i]], end=' ')
        print('\n')


def maratona():  # ERRO
    entry = input().strip().split()
    dist_interm_max = int(entry[1])  # metros
    pos_postos_agua = list(map(int, input().strip().split()))  # metros
    dist_maratona = 42195  # metros
    dif = 0
    for posto in pos_postos_agua:
        if posto == pos_postos_agua[-1]:
            dif = dist_maratona - posto
        else:
            dif = posto - dif
        if dist_interm_max >= dif:
            consegue_terminar = True
        else:
            consegue_terminar = False
            break
    print('S') if consegue_terminar else print('N')


def pulo_do_sapo():  # OK
    num_pedras, num_sapos = map(int, input().strip().split())
    pedras_lista = []
    for pedra in range(1, num_pedras+1):
        pedras_lista.append(pedra)
    possibs = []
    for sapo in range(0, num_sapos):
        pos_inicial, dist_fixa = map(int, input().strip().split())
        possibs.append(pos_inicial)
        possib_pedra = pos_inicial
        while True:
            possib_pedra -= dist_fixa
            if possib_pedra >= 1:
                possibs.append(possib_pedra)
            else:
                break
        possib_pedra = pos_inicial
        while True:
            possib_pedra += dist_fixa
            if possib_pedra <= num_pedras + 1:
                possibs.append(possib_pedra)
            else:
                break
    possibs = sorted(possibs)
    for i in range(0, num_pedras):
        print('1') if pedras_lista[i] in possibs else print('0')


def campo_minado():  # OK
    qtd_minas = int(input())
    total_mines = []
    for mina in range(0, qtd_minas):
        is_mine = int(input())
        total_mines.append(is_mine)
        # só somar: anterior + atual + proximo
    for i, mine in enumerate(total_mines):
        sum = 0
        if len(total_mines) > 1:
            if i == 0:
                sum = mine + total_mines[i+1]
                # print(sum, 1)
            elif i == len(total_mines)-1:
                sum = total_mines[i-1] + mine
                # print(sum, 2)
            else:
                sum = total_mines[i-1] + mine + total_mines[i+1]
                # print(sum, 3)
        print(sum)




sansas_snow_castle()
