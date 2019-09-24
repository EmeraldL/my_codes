N = int(input())
cont = 0
while cont < N:
    XY = input()
    XY = XY.split(' ')
    X = int(XY[0])
    Y = int(XY[1])
    if X > Y:
        y = X
        x = Y
    else:
        x = X
        y = Y
        
    soma = 0
    for i in range(x+1,y):
        if i%2 != 0:
            soma = soma + i
    print(soma)
    cont = cont + 1
