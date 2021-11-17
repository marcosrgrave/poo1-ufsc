def selection_test_1():
    pass


def interval():
    pass


def snack():
    prices = [4, 4.5, 5, 2, 1.5]
    entry = input().strip().split()
    code = int(entry[0])
    amount = int(entry[1])
    total = prices[code - 1] * amount
    print(f'Total: R$ {total:.2f}')


def average3():
    notas = input().split()
    nota1 = float(notas[0])
    nota2 = float(notas[1])
    nota3 = float(notas[2])
    nota4 = float(notas[3])

    # nota1 = float(input())
    # nota2 = float(input())
    # nota3 = float(input())
    # nota4 = float(input())

    # notas = [nota1, nota2, nota3, nota4]
    # notas = [2.0, 4.0, 7.5, 8.0]
    pesos = [2, 3, 4, 1]

    soma = 0
    for i, nota in enumerate(notas):
        soma += nota * pesos[i]
    media = soma / sum(pesos)

    exame = False
    if media >= 7:
        status = 'Aluno aprovado.'
    elif media < 7 and media > 5:
        status = 'Aluno em exame.'
        exame = True
    else:
        status = 'Aluno reprovado.'

    # print(f'Media: {media:.1f}\n{status}')
    print('Media: ' + "%.1f" % media + '\n' + status)

    if exame:
        # nota_exame = float(input())
        nota_exame = 6.4
        media = (media + nota_exame) / 2
        status = 'Aluno aprovado.' if media >= 5 else 'Aluno reprovado.'

        # print(f'Nota do exame: {nota_exame:.1f}\n{status}\nMedia final: {media:.1f}')
        print('Nota do exame: ' + "%.1f" % nota_exame + '\n' + status + '\n' + 'Media final: ' + "%.1f" % media)


def triangle():
    A = float(input())
    B = float(input())
    C = float(input())

    testeA = abs(B - C) < A < (B + C)
    testeB = abs(A - C) < B < (A + C)
    testeC = abs(A - B) < C < (A + B)

    if testeA and testeB and testeC:
        perimeter = A + B + C
        print(f"Perimetro = {perimeter:.1f}")
    else:
        area = ((A + B) / 2) * C
        print(f"Area = {area:.1f}")


def multiples():
    entry = input().split()
    A = int(entry[0])  # 6 #int(input())
    B = int(entry[1])  # 25 #int(input())
    print('Sao Multiplos') if B % A == 0 or A % B == 0 else print('Nao sao Multiplos')


def animal():
    pass


def wich_triangle():
    pass


def avioes_de_papel():
    entry = input().strip().split()
    qtd_compet = int(entry[0])
    qtd_folhas_compradas = int(entry[1])
    qtd_folhas_necessarias = int(entry[2])

    print('S') if qtd_compet*qtd_folhas_necessarias <= qtd_folhas_compradas else print('N')


def sedex():
    diametro_bola = int(input())

    dimensoes_cx = input().strip().split()
    alt_cx = int(dimensoes_cx[0])
    larg_cx = int(dimensoes_cx[1])
    prof_cx = int(dimensoes_cx[2])

    print('S') if diametro_bola <= alt_cx and diametro_bola <= larg_cx and diametro_bola <= prof_cx else print('N')


def sedex_marciano():
    entry = input().strip().split()
    x = int(entry[0])
    y = int(entry[1])
    z = int(entry[2])
    raio = int(entry[3])

    print('S') if raio**2 >= x**2/4 + y**2/4 and raio**2 >= x**2/4 + z**2/4 and raio**2 >= y**2/4 + z**2/4 else print('N')


def vice_campeao():
    entry = input().split()
    entry_int = []
    for v in entry:
        entry_int.append(int(v))
    print(sorted(entry_int)[1])


def colchao():
    pass


def campeonato():
    entry = input().strip().split()
    Cv, Ce, Cs, Fv, Fe, Fs = int(entry[0]), int(entry[1]), int(entry[2]), int(entry[3]), int(entry[4]), int(entry[5])
    pts_C = Cv*3 + Ce
    pts_F = Fv*3 + Fe
    if pts_C > pts_F:
        print('C')
    elif pts_C == pts_F:
        if Cs > Fs:
            print('C')
        elif Cs == Fs:
            print('=')
        else:
            print('F')
    else:
        print('F')


def corrida():
    pass


campeonato()
# -*- coding: utf-8 -*-
