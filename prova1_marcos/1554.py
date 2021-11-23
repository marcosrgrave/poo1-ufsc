# Input da quantidade de test_cases
test_cases = int(input())

# Vetor em que serão armazenadas as respostas
resps = []

# Criando um processo que se repetirá para cada test_case
for test_case in range(0, test_cases):
    
    available_balls = int(input())  # input de quantas bolas estão na mesa, além da branca
    dist = []  # vetor que armazenará a distância encontrada das bolas coloridas à branca
    x = []  # vetor que armazenará a coordenada x de cada bola colorida
    y = []  # vetor que armazenará a coordenada y de cada bola colorida
    
    # Criando uma repetição para cada bola (branca e colorida)
    for ball in range(0, available_balls+1):
        
        coord = input().strip().split()  # input das coordenadas x e y da determinada bola
        x.append(int(coord[0]))  # adicionando a coordenada x dessa bola ao vetor das coordenadas x para esse test_case
        y.append(int(coord[1]))  # adicionando a coordenada y dessa bola ao vetor das coordenadas y para esse test_case
        
        # Calculando a distancia da bola colorida à branca
        if ball > 0:  # filtrando a bola branca, para pegar apenas as coloridas
            d = ((y[0]-y[ball])**2 + (x[0]-x[ball])**2)**(1/2)  # a distância corresponde ao cálculo da hipotenusa formado pela diferença entre as coordenadas x e y das bola colorida e branca
            dist.append(d)  # adicionando a distancia encontrada ao vetor

    # Adicionando a menor distancia encontrada da bola branca no vetor 'dist' ao vetor das respostas
    resps.append(dist.index(min(dist))+1)

# Printando as respostas armazenadas
for r in resps:
    print(r)
