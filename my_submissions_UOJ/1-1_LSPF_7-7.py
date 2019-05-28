N = []
T = int(input())

while T<2 or T>50:
    T = int(input())

posicao = 0
for j in range (0,1000):
    N.append(posicao)
    print("N[%d] = %d" %(j, posicao))
    posicao = posicao+1
    if posicao==T:
        posicao = 0
