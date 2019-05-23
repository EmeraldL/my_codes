X = int(input())
Y = int(input())

if Y < X:
    x = Y-1
    y = X
elif X < Y:
    x = X-1
    y = Y

soma = 0

while x < y:
    x = x+1

    if x%13!=0:
        soma = soma+x

print(soma)
