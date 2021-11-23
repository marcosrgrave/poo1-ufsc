# Input
test_cases = int(input())

# Vetor em que serão armazenadas as respostas
resps = []

# Criando uma repetição para cada test_case
for test_case in range(0, test_cases):
    available_balls = int(input())
    dist = []
    x = []
    y = []
    for ball in range(0, available_balls+1):
        coord = input().strip().split()
        x.append(int(coord[0]))
        y.append(int(coord[1]))
        if ball > 0:
            d = ((y[0]-y[ball])**2 + (x[0]-x[ball])**2)**(1/2)
            dist.append(d)

    # Adicionando o indice no vetor 'dist' que representa a menor distancia encontrada da bola branca
    resps.append(dist.index(min(dist))+1)

for r in resps:
    print(r)
