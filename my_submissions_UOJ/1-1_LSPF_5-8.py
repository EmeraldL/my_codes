N = int(input())
cont = 0

while cont<N:
    XY = input()
    XY = XY.split(" ")
    X = int(XY[0])
    Y = int(XY[1])
    soma = 0
    y = 0
    while y<Y:
        if X%2 == 0:
            X = X+1
        if X%2 != 0:
            soma = soma + X
            X = X+1
            y = y+1
    print(soma)
    cont = cont+1
