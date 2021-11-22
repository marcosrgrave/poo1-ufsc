def selection_test_1():
    entry = input().strip().split()
    A = int(entry[0])
    B = int(entry[1])
    C = int(entry[2])
    D = int(entry[3])

    test1 = B > C and D > A
    test2 = C + D > A + B
    test3 = C > 0 and D > 0 and A % 2 == 0
    print('Valores aceitos') if test1 and test2 and test3 else print('Valores nao aceitos')


def interval():
    n = float(input())
    vs = [25, 50, 75, 100]

    if n < 0 or n > 100:
        print('Fora de intervalo')
    else:
        if n >= 0 and n <= 25:
            print('Intervalo [0,25]')
        else:
            for i, v in enumerate(vs):
                if i+1 < len(vs):
                    if n > vs[i] and n <= vs[i+1]:
                        print(f'Intervalo ({vs[i]},{vs[i+1]}]')


def snack():
    prices = [4, 4.5, 5, 2, 1.5]
    entry = input().strip().split()
    code = int(entry[0])
    amount = int(entry[1])
    total = prices[code - 1] * amount
    print(f'Total: R$ {total:.2f}')


def average3():
    notas = input().split()
    pesos = [2, 3, 4, 1]

    soma = 0
    for i, nota in enumerate(notas):
        soma += float(nota) * pesos[i]
    media = soma / sum(pesos)

    exame = False
    if media >= 7:
        status = 'Aluno aprovado.'
    elif 7 > media > 5:
        status = 'Aluno em exame.'
        exame = True
        nota_exame = float(input())
        media_exame = (media + nota_exame) / 2
        status_exame = 'Aluno aprovado.' if media >= 5 else 'Aluno reprovado.'
    else:
        status = 'Aluno reprovado.'

    print(f'Media: {media:.1f}\n{status}')
    if exame:
        print(f'Nota do exame: {nota_exame:.1f}\n{status_exame}\nMedia final: {media_exame:.1f}')


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
    dado1 = input()
    dado2 = input()
    dado3 = input()

    if dado1 == 'vertebrado':
        if dado2 == 'ave':
            print('aguia') if dado3 == 'carnivoro' else print('pomba')
        else:
            print('homem') if dado3 == 'onivoro' else print('vaca')
    else:
        if dado2 == 'inseto':
            print('pulga') if dado3 == 'hematofago' else print('lagarta')
        else:
            print('sanguessuga') if dado3 == 'hematofago' else print('minhoca')


def wich_triangle():
    entry = input().split()
    A = int(entry[0])
    B = int(entry[1])
    C = int(entry[2])

    testeA = abs(B - C) < A < (B + C)
    testeB = abs(A - C) < B < (A + C)
    testeC = abs(A - B) < C < (A + B)

    valido = True if testeA and testeB and testeC else False
    isoceles = True if A == B or A == C or B == C else False
    equilatero = True if A == B == C else False

    entry_int = []
    for v in entry:
        entry_int.append(int(v))
    retangulo = True if max(A, B, C) ** 2 == sorted(entry_int)[0] ** 2 + sorted(entry_int)[1] ** 2 else False

    if valido:
        if isoceles:
            print('Valido-Isoceles')
            print('Retangulo: S') if retangulo else print('Retangulo: N')
        elif equilatero:
            print('Valido-Equilatero')
            print('Retangulo: S') if retangulo else print('Retangulo: N')
        else:
            print('Valido-Escaleno')
            print('Retangulo: S') if retangulo else print('Retangulo: N')
    else:
        print('Invalido')


def avioes_de_papel():
    entry = input().strip().split()
    qtd_compet = int(entry[0])
    qtd_folhas_compradas = int(entry[1])
    qtd_folhas_necessarias = int(entry[2])

    print('S') if qtd_compet * qtd_folhas_necessarias <= qtd_folhas_compradas else print('N')


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

    print(
        'S') if raio ** 2 >= x ** 2 / 4 + y ** 2 / 4 and raio ** 2 >= x ** 2 / 4 + z ** 2 / 4 and raio ** 2 >= y ** 2 / 4 + z ** 2 / 4 else print(
        'N')


def vice_campeao():
    entry = input().split()
    entry_int = []
    for v in entry:
        entry_int.append(int(v))
    print(sorted(entry_int)[1])


def colchao():
    dimensoes_colchao = sorted(map(int, input().split()))
    dimensoes_porta = sorted(map(int, input().split()))

    if dimensoes_colchao[0] <= dimensoes_porta[0] and dimensoes_colchao[1] <= dimensoes_porta[1]:
        print('S')
    else:
        print('N')


def campeonato():
    entry = input().strip().split()
    Cv, Ce, Cs, Fv, Fe, Fs = int(entry[0]), int(entry[1]), int(entry[2]), int(entry[3]), int(entry[4]), int(entry[5])
    pts_C = Cv * 3 + Ce
    pts_F = Fv * 3 + Fe
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
    charrete1 = input().strip().split()
    n1 = int(charrete1[0])  # numero da charrete
    d1 = int(charrete1[1])  # distancia em metros
    v1 = int(charrete1[2])  # velocidade em km/h

    v1_ms = v1 / 3.6
    t1 = d1 / v1_ms

    charrete2 = input().strip().split()
    n2 = int(charrete2[0])
    d2 = int(charrete2[1])
    v2 = int(charrete2[2])

    v2_ms = v2 / 3.6
    t2 = d2 / v2_ms

    print(n1) if t1 < t2 else print(n2)


average3()
# -*- coding: utf-8 -*-
