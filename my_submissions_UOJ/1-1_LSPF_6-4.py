N = int(input())
while N<0 or N>20:
    N = int(input())

cont = 1
while cont<=N:
    X = int(input())
    while X<0 or X>10**8:
        X = int(input())

    soma = 0
    for i in range (1,X):
        if X%i==0:
            soma = soma+i

    if soma==X:
        print(str(X)+" eh perfeito")
    else:
        print(str(X)+" nao eh perfeito")
    cont = cont+1
