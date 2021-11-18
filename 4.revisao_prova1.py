def quadrant():
    respostas = []
    while True:
        entry = input().split()
        X = int(entry[0])
        Y = int(entry[1])
        if X == 0 or Y == 0:
            break
        if X>0 and Y>0:
            respostas.append('primeiro')
        elif X<0 and Y>0:
            respostas.append('segundo')
        elif X<0 and Y<0:
            respostas.append('terceiro')
        else:
            respostas.append('quarto')

    for resposta in respostas:
        print(resposta)


def what_is_the_fastest():
    pass


def capuchin_monkey():
    pass


def bafo():
    pass


def easy_diff_btwn_dates():
    pass


def elevator():
    pass


def escada_rolante():
    pass


def album_fotos():
    pass


def chocolate():
    pass


def saldo_do_vovo():
    pass


def old_clock():
    pass


def kikoho():
    pass


quadrant()
