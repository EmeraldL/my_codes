A = []

for j in range (0,100):
    V = float(input())
    A.append(V)

posicao = 0
for k in A:
    if k<=10:
        print("A[%d] = %2.1f" %(posicao,k))
    posicao = posicao+1
