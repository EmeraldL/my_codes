X = []

for j in range (10):
    valor = int(input())
    X.append(valor)

posicao = 0
for i in X:
    
    if i==0 or i<0:
        X[posicao] = 1
    
    posicao = posicao + 1

posicao = 0
for i in X:
    print("X[%d] = %d" %(posicao,i))
    posicao = posicao+1
