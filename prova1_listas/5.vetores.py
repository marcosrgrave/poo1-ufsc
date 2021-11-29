def musical_loop():
    '''
    se a diferença entre o input3 e o input2 for de mesmo sinal que a
    diferença entre input1 e input2, significa que nao houve um peak,
    caso sim, houve peak
    '''
    t = int(input())
    vet_list = list(map(int, input().strip().split()))
    

    for i, v in enumerate(vet_list):
        if vet_list[i+1] > v:
            sentido = up
        elif vet_list[i+1] < v:
            sentido = down
        else:
            continue

        
        if sentido == 0:
            pass
    
    
    for i, v in enumerate(vet_list):
        if v == vet_list[1] or v == vet_list[-1]:
            print(v)
            continue
        else:
            dif = vet_list[i+1] - v


def optical_reader():
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


def lowest_number_and_position():
    int(input())
    numbers = list(map(int, input().strip().split()))
    r = min(numbers)
    i = numbers.index(r)
    print(f'Menor valor: {r}\nPosicao: {i}')
    

def fake_tickets():
    pass


def XXXXXXXXXXXXXX():
    pass


def XXXXXXXXXXXXXX():
    pass


def XXXXXXXXXXXXXX():
    pass


def XXXXXXXXXXXXXX():
    pass




lowest_number_and_position()
