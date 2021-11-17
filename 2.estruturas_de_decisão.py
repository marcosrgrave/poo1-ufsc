def average3():
    notas = input().split()
    nota1 = float(notas[0])
    nota2 = float(notas[1])
    nota3 = float(notas[2])
    nota4 = float(notas[3])
    
    #nota1 = float(input())
    #nota2 = float(input())
    #nota3 = float(input())
    #nota4 = float(input())
    
    #notas = [nota1, nota2, nota3, nota4]
    #notas = [2.0, 4.0, 7.5, 8.0]
    pesos = [2, 3, 4, 1]



    soma = 0
    for i, nota in enumerate(notas):
        soma += nota*pesos[i]
    media = soma/ sum(pesos)
    
    exame = False
    if media >= 7:
        status = 'Aluno aprovado.'
    elif media < 7 and media > 5:
        status = 'Aluno em exame.'
        exame = True
    else:
        status = 'Aluno reprovado.'
    
    #print(f'Media: {media:.1f}\n{status}')
    print('Media: ' + "%.1f" % media +'\n'+ status)



    if exame:
        #nota_exame = float(input())
        nota_exame = 6.4
        media = (media+nota_exame)/2
        status='Aluno aprovado.' if media >= 5 else 'Aluno reprovado.'

        #print(f'Nota do exame: {nota_exame:.1f}\n{status}\nMedia final: {media:.1f}')
        print('Nota do exame: ' + "%.1f" % nota_exame +'\n'+ status + '\n' + 'Media final: ' + "%.1f" % media)


def triangle():
    A = float(input())
    B = float(input())
    C = float(input())
    
    testeA = abs(B-C) < A < (B+C)
    testeB = abs(A-C) < B < (A+C)
    testeC = abs(A-B) < C < (A+B)
    
    if testeA and testeB and testeC:
        perimeter = A+B+C
        print(f"Perimetro = {perimeter:.1f}")
    else:
        area = ((A+B)/2)*C
        print(f"Area = {area:.1f}")
    
    
    
def teste():
    nao_vetor = 'atemoia'
    vetor = nao_vetor.split()
    print(nao_vetor, vetor)
    float_teste = 3.222
    print(f'{float_teste:.2f}')
    print("%.2f" % float_teste)
    
    
def multiples():
    entry = input().split()
    A = int(entry[0]) #6 #int(input())
    B = int(entry[1])#25 #int(input())
    print('Sao Multiplos') if B % A == 0 or A % B == 0 else print('Nao sao Multiplos')
    
multiples()