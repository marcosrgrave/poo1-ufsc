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


def wertyu():  # Ok
    QWERTY = {
        '1': "`", '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6',
        '8': '7', '9': '8', '0': '9', '-': '0', '=': '-', 'I': 'U', 'W': 'Q', 
        'E': 'W', 'R': 'E', 'T': 'R', 'Y': 'T', 'U': 'Y', 'H': 'G', 'J': 'H',
        'O': 'I', 'P': 'O', 'S': 'A', 'D': 'S', 'F': 'D', 'G': 'F', 'M': 'N',
        'K': 'J', 'L': 'K', 'X': 'Z', 'C': 'X', 'V': 'C', 'B': 'V', 'N': 'B',
        ',': 'M', '.': ',', '/': '.', ' ': ' ', '[': 'P', ']': '[', "\\": ']',
        ';': 'L', "'": ';', 'A': '', 'Q': '', 'Z': '', '`': ''
    }

    while True:
        try:
            txt = input()
            for char in txt:
                print(' ', end='') if char == ' ' else print(
                    QWERTY[char], end='')
            print()
        except EOFError:
            break

    # Outra maneira seria:
        # try:
            # txt = input()
            # answer = ''
            # for char in txt:
            #     answer += QWERTY[char]
            # print(answer)
        # except EOFError:
            # break

    # Já essa maneira talvez n dê certo:
        # querty = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
        # try:
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
    test_cases: int = int(input())
    for test in range(test_cases):
        words: str = input().strip().split()
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


def binary_watch():  # Acho que é erro de formatacao.
    def decimal_to_binary(decimal):  # 6 bits max
        powers = [32, 16, 8, 4, 2, 1]
        binary_number = ''
        s = 0
        # decimal = 36
        for pow in powers:
            if pow <= decimal and pow + s <= decimal:
                binary_number += '1'
                s += pow
            else:
                binary_number += '0'
        return binary_number
        
    
    while True:
        hour, minutes = map(int, input().split(':'))
        if hour + minutes == 0:
            break
        
        hour_bin = decimal_to_binary(hour).replace('0', ' ').replace('1', 'o')
        minutes_bin = decimal_to_binary(minutes).replace('0', ' ').replace('1', 'o')

        print(f''' ____________________________________________
|                                            |
|    ____________________________________    |_
|   |                                    |   |_)
|   |   8         4         2         1  |   |
|   |                                    |   |
|   |   {hour_bin[2]}         {hour_bin[3]}         {hour_bin[4]}         {hour_bin[5]}  |   |
|   |                                    |   |
|   |                                    |   |
|   |   {minutes_bin[0]}     {minutes_bin[1]}     {minutes_bin[2]}     {minutes_bin[3]}     {minutes_bin[4]}     {minutes_bin[5]}  |   |
|   |                                    |   |
|   |   32    16    8     4     2     1  |   |_
|   |____________________________________|   |_)
|                                            |
|____________________________________________|
''')

    print(f''' ____________________________________________
|                                            |
|    ____________________________________    |_
|   |                                    |   |_)
|   |   8         4         2         1  |   |
|   |                                    |   |
|   |                                    |   |
|   |                                    |   |
|   |                                    |   |
|   |                                    |   |
|   |                                    |   |
|   |   32    16    8     4     2     1  |   |_
|   |____________________________________|   |_)
|                                            |
|____________________________________________|
''')


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


def the_martian():  # Ok
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    HEX_PAIRS = ['61', '62', '63', '64', '65', '66', '67', '68', '69', '6A', '6B', '6C',
                 '6D', '6E', '6F', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A']

    int(input())  # nao usa pra nada
    pairs = input().split()

    for pair in pairs:
        i = HEX_PAIRS.index(pair)
        print(ALPHABET[i], end='')
    print()


def name_at_form():  # Ok
    txt = input()
    print('YES') if len(txt) <= 80 else print('NO')


def banco_imobiliario():  # Ok
    PLAYERS = 'D', 'E', 'F'

    initial_money, num_operations = map(int, input().split())
    players_money = [initial_money, initial_money, initial_money]

    for operation in range(num_operations):
        entry = input()
        action: str = entry[0]

        if action == 'A':  # Aluguel
            not_used, plus_player, minus_player, amount = entry.split()

            i_plus = PLAYERS.index(plus_player)
            players_money[i_plus] += int(amount)

            i_minus = PLAYERS.index(minus_player)
            players_money[i_minus] -= int(amount)
        else:
            not_used, player, amount = entry.split()
            if action == 'C':  # Compra
                i = PLAYERS.index(player)
                players_money[i] -= int(amount)
            else:  # Venda
                i = PLAYERS.index(player)
                players_money[i] += int(amount)

    print(players_money[0], players_money[1], players_money[2])


def lingua_do_p():  # Ok
    txt = input()
    next_is_p = False
    for i in range(len(txt)):
        if not next_is_p:
            if i == len(txt)-1 and txt[i] != 'p':
                print(txt[i], end='')
            elif txt[i] != 'p':
                print(txt[i], end='')
            elif txt[i+1] == 'p':
                print(txt[i], end='')
                next_is_p = True
        else:
            next_is_p = False


def letras():  # Ok
    char: str = input().strip()  # o segredo tá no strip()
    txt: str = input().strip().split()
    s: int = 0
    for word in txt:
        if char in word:
            s += 1
    print(f'{s/len(txt)*100:.1f}')


def new_password_ra():  # Ok
    dic: dict = {
        'GQaku': 0,
        'ISblv': 1,
        'EOYcmw': 2,
        'FPZdnx': 3,
        'JTeoy': 4,
        'DNXfpz': 5,
        'AKUgq': 6,
        'CMWhr': 7,
        'BLVis': 8,
        'HRjt': 9,
    }

    tests: int = int(input())
    for t in range(tests):
        c = 0
        password: str = input().strip()
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
    '''
    he never gets wet;
    he never has to carry an umbrella if it's not raining.
    '''

    tests: int = int(input())
    need_umbrella: bool = False
    sum_ida = sum_volta = 0
    for t in range(tests):
        ida, volta = input().strip().split()

        if need_umbrella and ida == 'sol':
            need_umbrella = False

        elif not need_umbrella and ida == 'chuva':
            need_umbrella = True
            sum_ida += 1

        if need_umbrella and volta == 'sol':
            need_umbrella = False

        elif not need_umbrella and volta == 'chuva':
            need_umbrella = True
            sum_volta += 1

    print(sum_ida, sum_volta)

    # ...LOGICA AQUI...


def lexical():  # Ok
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    wordA = input().strip()
    wordB = input().strip()

    if wordA in wordB or wordB in wordA:
        print(f'{min(wordA, wordB)}\n{max(wordA, wordB)}')
    else:
        for i in range(max(len(wordA), len(wordB))):
            if wordA[i] == wordB[i]:
                continue
            else:
                if alphabet.index(wordA[i]) < alphabet.index(wordB[i]):
                    print(f'{wordA}\n{wordB}')
                else:
                    print(f'{wordB}\n{wordA}')
                break


def cryptotext():  # Ok
    test_cases = int(input().strip())
    for t in range(test_cases):
        txt = input().strip()
        secret_word = []

        for i in range(len(txt)-1, -1, -1):
            if txt[i].islower():
                print(txt[i], end='')
        print()


def binary_phrase():  # Acho que é erro de formatacao.
    # Acho que pode estar faltando uma quebra linha ou algo assim.
    # https://www.rapidtables.com/convert/number/ascii-to-binary.html
    # https://www.browserling.com/tools/spaces-to-newlines
    
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'  # 65 ao 90
    alphabet_upper = alphabet_lower.upper()  # 97 ao 122

    while True:
        try:
            phrase = int(input().strip())
            for char in range(phrase):
                binary = input().strip()
                decimal = 0
                for i in range(len(binary)):
                    if binary[-i-1] == '1':
                        decimal += 2**i
                if 65 <= decimal <= 90:
                    print(alphabet_upper[decimal-65], end='')
                elif 97 <= decimal <= 122:
                    print(alphabet_lower[decimal-97], end='')
                # elif decimal == 32:
                else:
                    print(' ', end='')
            print('\n', end='')

        except EOFError:
            break
    
    # INPUTS:
        # 9
        # 1101011
        # 1100101
        # 1100101
        # 1110000
        # 100000
        # 1100011
        # 1100001
        # 1101100
        # 1101101
        # 1
        # 1100101
        # 105
        # 01001100
        # 01101111
        # 01110010
        # 01100101
        # 01101101
        # 00100000
        # 01101001
        # 01110000
        # 01110011
        # 01110101
        # 01101101
        # 00100000
        # 01100100
        # 01101111
        # 01101100
        # 01101111
        # 01110010
        # 00100000
        # 01110011
        # 01101001
        # 01110100
        # 00100000
        # 01100001
        # 01101101
        # 01100101
        # 01110100
        # 00100000
        # 00100000
        # 01100011
        # 01101111
        # 01101110
        # 01110011
        # 01100101
        # 01100011
        # 01110100
        # 01100101
        # 01110100
        # 01110101
        # 01110010
        # 00100000
        # 01100001
        # 01100100
        # 01101001
        # 01110000
        # 01101001
        # 01110011
        # 01100011
        # 01101001
        # 01101110
        # 01100111
        # 00100000
        # 01100101
        # 01101100
        # 01101001
        # 01110100
        # 00100000
        # 00100000
        # 01000011
        # 01110101
        # 01110010
        # 01100001
        # 01100010
        # 01101001
        # 01110100
        # 01110101
        # 01110010
        # 00100000
        # 01100100
        # 01100001
        # 01110000
        # 01101001
        # 01100010
        # 01110101
        # 01110011
        # 00100000
        # 01101110
        # 01110101
        # 01101100
        # 01101100
        # 01100001
        # 00100000
        # 01100001
        # 00100000
        # 01110110
        # 01100101
        # 01101100
        # 01101001
        # 01110100
        # 00100000
        # 01100101
        # 01100111
        # 01100101
        # 01110011
        # 01110100
        # 01100001
        # 01110011
        # 00100000
        # 01100001
        # 01100011
        # 01100011
        # 01110101
        # 01101101
        # 01110011
        # 01100001
        # 01101110

binary_watch()
