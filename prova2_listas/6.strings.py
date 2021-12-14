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


def wertyu():  # INCOMPLETO
    # tá faltando um print na ultima linha de todas (udebug)
    while True:
        try:
            querty = {'1':"`", '2':'1', '3':'2', '4':'3', '5':'4','6':'5',
                '7':'6', '8':'7', '9':'8', '0':'9', '-':'0','=':'-',
                'W':'Q','E':'W','R':'E','T':'R','Y':'T','U':'Y', 'I':'U',
                'O':'I','P':'O','S':'A','D':'S','F':'D','G':'F','H':'G','J':'H',
                'K':'J','L':'K','X':'Z','C':'X','V':'C','B':'V','N':'B','M':'N',
                ',':'M','.':',','/':'.', ' ':' ', '[':'P',']':'[','\\':']',
                ';':'L',"'":';', 'A':'', 'Q':'', 'Z':'', '`':''}
            txt = input().strip()
            for char in txt:
                print(' ', end='') if char == ' ' else print(querty[char], end='')
            print()
        except EOFError:
            break


            # querty = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
            # txt = input().strip()
            # for char in txt:
            #     if char == ' ':
            #         print(' ', end='')
            #     else:
            #         i = querty.index(char.upper())
            #         print(querty[i-1], end='')
            # print()
        # except EOFError:
        #     break


def combiner():  # OK
    test_cases : int = int(input())
    for test in range(test_cases):
        words : str = input().strip().split()
        for i in range(max(len(words[0]), len(words[1]))):
            if i < len(words[0]):
                print(words[0][i], end='')
            if i < len(words[1]):
                print(words[1][i], end='')
        print()


def lost_boots():  # OK
    while True:
        try:
            tests = int(input())
            d_sizes, e_sizes, pairs = [], [], []
            for t in range(tests):
                boot_size, foot = input().strip().split()
                if foot == 'D':
                    if boot_size in e_sizes:
                        pairs.append([boot_size, boot_size])
                        e_sizes.remove(boot_size)
                    else:
                        d_sizes.append(boot_size)
                else:
                    if boot_size in d_sizes:
                        pairs.append([boot_size, boot_size])
                        d_sizes.remove(boot_size)
                    else:
                        e_sizes.append(boot_size)
            # print(pairs)
            print(len(pairs))
        except EOFError:
            break


def binary_watch():  # FALTA FAZER
    print(f''' ____________________________________________
    |                                            |
    |    ____________________________________    |_
    |   |                                    |   |_)
    |   |   8         4         2         1  |   |
    |   |                                    |   |
    |   |  {'o'}        {'o'}                      |   |
    |   |                                    |   |
    |   |                                    |   |
    |   |         o                          |   |
    |   |                                    |   |
    |   |   32    16    8     4     2     1  |   |_
    |   |____________________________________|   |_)
    |                                            |
    |____________________________________________|''')


def deli_deli():  # OK
    qtd_description, qtd_test_words = map(int, input().strip().split())
    sings, plurs = [], []
    for desc in range(qtd_description):
        singular, plural = input().strip().split()
        sings.append(singular)
        plurs.append(plural)
    for test in range(qtd_test_words):
        word = input()
        if word in sings:
            i = sings.index(word)
            print(plurs[i])
        elif word[-2] not in 'aeiou' and word[-1] == 'y':
            print(word.replace('y', 'ies'))
        elif word[-1] in 'osx' or word[-2:] in 'ch' or word[-2:] in 'sh':
            print(word.__add__('es'))
        else:
            print(word.__add__('s'))


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


the_martian()