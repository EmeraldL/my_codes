X = int(input())

while X != 0:
    
    soma = 0
    cont = 0
    while cont < 5:
        if X%2 == 0:
            soma = soma + X
            X = X + 1
            cont = cont + 1
        else:
            X = X + 1
    print(soma)
    X = int(input())
