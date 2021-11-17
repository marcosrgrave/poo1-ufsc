def banknotes_and_coins():
    pass
    
    
def even_numbers():
    for number in range(1, 100+1):
        if number % 2 == 0:
            print(number)
    
    
def odd_numbers():
    x = int(input())
    for number in range(0, x+1):
        if (number+1) % 2 == 0:
            print(number)
    
    
def even_square():
    x = 6#int(input())
    for number in range(1, x+1):
        if number % 2 == 0:
            print(f'{number}^2 = {number**2}')
    
    
def even_or_odd():
    test_cases = 4#int(input())
    for case in range(0, test_cases):
        number = int(input())
        if number == 0:
            print('NULL')
        elif (even:= number % 2 == 0):
            print('EVEN POSITIVE') if (positive:= number > 0) else print('EVEN NEGATIVE')
        else:
            print('ODD POSITIVE') if (positive:= number > 0) else print('ODD NEGATIVE')
        
        
def remaining2():
    N = 13#int(input())
    for number in range(1, 1000+1):
        if number % N == 2:
            print(number)
    
    
def multiplication_table():
    N = int(input())
    for number in range(1, 10+1):
        result_mult = N*number
        print(f'{number} x {N} = {result_mult}')
        
        
def highest_and_position():
    maxim = 0
    for i in range(0, 100):
        number = int(input())
        if number > maxim:
            maxim = number
            pos = i+1
    print(maxim)
    print(pos)
    
    
def queen():
    pass
    #board = [8, 8]
    
    
def sum_of_consecutive_odd_numbersII():
    test_cases = 3#int(input())
    for test_case in range(0, test_cases):
        X = 10#int(input())
        Y = 15#int(input())
        soma = 0
        for number in range(X, Y):
            if (odd:= (number+1) % 2 ==0):
                soma += number
        print(soma)
    
    
def fixed_password():
    while True:
        pswrd_try = input()
        if pswrd_try == '2002':
            print('Acesso Permitido')
            break
        else:
            print('Senha Invalida')
            continue
    
    
def type_of_fuel():
    #1. Alcohol 2. Gasoline 3. Diesel 4. End
    fuel_types = [1, 2, 3]
    soma_total = [0, 0, 0]
    while True:
        customer_fuel = int(input())
        if customer_fuel == 4:
            break
        elif customer_fuel in fuel_types:
            i = fuel_types.index(customer_fuel)
            soma_total[i] += 1
    print(f'MUITO OBRIGADO\nAlcool: {soma_total[0]}\nGasolina: {soma_total[1]}\nDiesel: {soma_total[2]}')
    
    
def fast_prime_number():
    pass
    
    
def feynman():
    pass
    
    
def zero_or_one():
    rodada = '0 1 0'.split()#input().split()
    rodada_int = []
    for v in rodada:
        rodada_int.append(int(v))
    players = ['A', 'B', 'C']
    
    sum0 = sum1 = 0
    for v in rodada_int:
        if v == 0:
            sum0 += 1
        else:
            sum1 += 1

    draw = False
    if sum0 == 1:
        (i:=rodada_int.index(0))
    elif sum1 == 1:
        (i:=rodada_int.index(1))
    else:
        draw = True
    print('*') if draw else print(players[i])
    
    
def pedro_christmas():
    from datetime import date
    
    entry = '12 26'.split()#input().split()
    month_data = int(entry[0])
    day_data = int(entry[1])
    
    date_input = date(2016, month_data, day_data)
    date_christmas = date(2016, 12, 25)
    dif = date_input - date_christmas
    if dif.days > 0:
        print('Ja passou!')
    elif dif.days == 0:
        print('E natal!')
    elif dif.days == -1:
        print('E vespera de natal!')
    else:
        print(f'Faltam {abs(dif.days)} dias para o natal!')
    
    #print(dif.days)
    
    
def bits_exchanged():
    bills = [50, 10, 5, 1]
    
    V = c = 1
    div = 0
    while V != 0:
        V = 72#abs(int(input()))
        print(f'Teste {c}')
        for bill in bills:
            div = V // bill
            V = V - div*bill
            print(div, end='')
        V = 1
        c += 1
        print('\n')
        
        if c == 6:
            V = 0
    
    
def folding():
    # Pra mim, os exemplos de input nao fazem sentido
    N = 2#int(input())  # times folding_operation_D was applied
    total_pieces = 4**N
    
    
def grandma():
    c = 1
    while c != 0:
        N = int(input())
        print(f'Teste {c}')
        sum_potA = sum_potB = 0
        for i in range(0, N):
            entry = input().split()
            potA = int(entry[0])
            potB = int(entry[1])
            
            sum_potA += potA
            sum_potB += potB
            dif = sum_potA - sum_potB
            print(dif)
        c += 1
        print('\n')
    
    
def garcom():
    pass
    
    
def tustin():
    pass
    
    
bits_exchanged()
# -*- coding: utf-8 -*-
