X = int(input())
Y = int(input())

if Y < X:
    x = Y
    y = X
elif X < Y:
    x = X
    y = Y
    
valor = x

while valor < (y-1):
    
    valor = valor+1
    
    if valor%5==2:
        print(valor)
        
    elif valor%5==3:
        print(valor)
