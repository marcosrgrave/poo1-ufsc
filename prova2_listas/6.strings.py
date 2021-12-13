def contract_revision():  # OK, MAS NAO CURTI O CODIGO
    # Acho que dá pra simplificar bem mais
    while True:
        failed_digit, number_in_contract = input().strip().split()
        if failed_digit == str(0) and number_in_contract == str(0):
            break
        
        final_answer = []
        for num_txt in number_in_contract:
            if num_txt != failed_digit:
                final_answer.append(int(num_txt))
        if sum(final_answer) == 0 or final_answer == []:
            print(0)
        else:
            comecou = False
            for digit in final_answer:
                if comecou:
                    print(digit, end='')
                elif digit != 0:
                    comecou = True
                    print(digit, end='')
            print()


def flowers_france():  # OK
    while True:
        phrase: str = input().strip().split()
        if '*' in phrase:
            break
        
        tautograms: bool = True
        for word in phrase:
            if word == phrase[0]:
                char = word[0]
            else:
                if char.upper() != word[0].upper():
                    tautograms = False
        print('Y') if tautograms else print('N')


def led():  # OK
    digit_led = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    #            0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    test_cases = int(input())
    for test in range(test_cases):
        s = 0
        number = input()
        for n in number:
            s += digit_led[int(n)]
        print(s, 'leds')


def wertyu():
    while True:
        try:
            querty = "1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
            txt = input().strip()
            for char in txt:
                if char == ' ':
                    print(' ', end='')
                else:
                    i = querty.index(char.upper())
                    print(querty[i-1], end='')
            print()
        except EOFError:
            break


def combiner():
    pass


def lost_boots():
    pass


def binary_watch():
    pass


def deli_deli():
    pass


def the_martian():
    pass


def name_at_form():
    pass


def banco_imobiliario():
    pass


def lingua_do_p():
    pass


def letras():
    pass


def new_password_ra():
    pass


def avoiding_rain():
    pass


def lexical():
    pass


def cryptotext():
    pass


def binary_phrase():
    pass


wertyu()