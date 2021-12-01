def musical_loop():
    '''
    se a diferença entre o input3 e o input2 for de mesmo sinal que a
    diferença entre input1 e input2, significa que nao houve um peak,
    caso sim, houve peak
    '''
    # t = int(input())
    # vet_list = list(map(int, input().strip().split()))
    

    # for i, v in enumerate(vet_list):
    #     if vet_list[i+1] > v:
    #         sentido = up
    #     elif vet_list[i+1] < v:
    #         sentido = down
    #     else:
    #         continue

        
    #     if sentido == 0:
    #         pass
    
    
    # for i, v in enumerate(vet_list):
    #     if v == vet_list[1] or v == vet_list[-1]:
    #         print(v)
    #         continue
    #     else:
    #         dif = vet_list[i+1] - v


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
    print(f'Menor valor: {r}\nPosicao: {i}')
    

def fake_tickets():
    while True:
        # MÉTODO 1 (NAO ROLA)
        # o, p = input().strip().split()
        # original_tickets, persons_attending = int(o), int(p)
        
        a = input().split()
        if '0' in a:
            break
        ticket_numbers = list(map(int, input().strip().split()))
        st = set(ticket_numbers)
        s = 0
        for v in ticket_numbers:
            if v in st:
                s += 1
        print(s - len(st))


def head_or_tail():  # TESTAR NO BEECROWD
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


def sticks_game():  # TESTAR NO BEECROWD
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
        else:
            four_sides = []
            two_sides = []

            for set in range(0, number_of_sets):
                size, amount = map(int, input().strip().split())
                if amount >= 4:
                    full = amount // 4
                    four_sides.append(full)
                elif amount >= 2:
                    half = amount // 2
                    two_sides.append(half)
                
            total_rectangles = sum(four_sides) + sum(two_sides)//2
            print(total_rectangles)


def XXXXXXXXXXXXXX():
    pass


def XXXXXXXXXXXXXX():
    pass




sticks_game()


from time import perf_counter
def start_code_time():
    return perf_counter()
    
def end_code_time(start_code_time):
    end_code = perf_counter()
    time_code = end_code - start_code_time
    return time_code
