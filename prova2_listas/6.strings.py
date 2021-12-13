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


def flowers_france():
    pass


def led():
    pass


def wertyu():
    pass


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


contract_revision()