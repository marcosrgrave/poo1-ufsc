def contract_revision():  # Ok, mas dá pra fazer bem melhor
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


def flowers_france():  # Ok
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


def led():  # Ok
    digit_led = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    #            0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    test_cases = int(input())
    for test in range(test_cases):
        s = 0
        number = input()
        for n in number:
            s += digit_led[int(n)]
        print(s, 'leds')


def wertyu():  # Presentation Error
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


def combiner():  # Ok
    test_cases : int = int(input())
    for test in range(test_cases):
        words : str = input().strip().split()
        for i in range(max(len(words[0]), len(words[1]))):
            if i < len(words[0]):
                print(words[0][i], end='')
            if i < len(words[1]):
                print(words[1][i], end='')
        print()


def lost_boots():  # Ok
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


def binary_watch():  # Falta Fazer
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


def deli_deli():  # Ok
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


def the_martian():  # Falta Fazer
    pass


def name_at_form():  # Ok
    txt = input()
    print('YES') if len(txt) <= 80 else print('NO')


def banco_imobiliario():  # Falta Fazer
    pass


def lingua_do_p():  # Presentation Error
    # No udebug consegui bater o resultado,
    # mas ainda assim n foi aprovado.
    txt = input()
    next_is_p = False
    for i in range(len(txt)):
        if not next_is_p:
            if i == len(txt)-1 and txt[i] != 'p':
                print(txt[i], end='\n')
            elif txt[i] != 'p':
                print(txt[i], end='')
            elif txt[i+1] == 'p':
                print(txt[i], end='')
                next_is_p = True
        else:
            next_is_p = False


def letras():  # Ok
    char : str = input().strip()  # o segredo tá no strip()
    txt : str = input().strip().split()
    s : int = 0
    for word in txt:
        if char in word:
            s += 1
    print(f'{s/len(txt)*100:.1f}')


def new_password_ra():  # Ok
    dic : dict = {
        'GQaku' : 0,
        'ISblv' : 1,
        'EOYcmw' : 2,
        'FPZdnx' : 3,
        'JTeoy' : 4,
        'DNXfpz' : 5,
        'AKUgq' : 6,
        'CMWhr' : 7,
        'BLVis' : 8,
        'HRjt' : 9,
    }
    
    tests : int = int(input())
    for t in range(tests):
        c = 0
        password : str = input().strip()
        for char in password:
            if c == 12:
                break
            keys = dic.keys()
            for key in keys:
                if char in key:
                    print(dic[key], end='')
                    c += 1
                    break
        print()


def avoiding_rain():  # Fazendo (Desenhar)
    tests : int = int(input())
    for t in range(tests):
        home, office = input().strip().split()

        # ...LOGICA AQUI...
        


def lexical():
    pass


def cryptotext():
    pass


def binary_phrase():
    pass


avoiding_rain()
