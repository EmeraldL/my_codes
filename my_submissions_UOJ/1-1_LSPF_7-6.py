T = int(input())

#Sequência de Fibonacci
Fib = [0,1]
posant1 = Fib[1]
posant2 = Fib[0]

for i in range(2,61):
    Fib.insert(i, (posant1 + posant2))
    posant1 = Fib[i]
    posant2 = Fib[i-1]

cont = 1
while cont <= T:
    N = int(input())
    while N<0 or N>60:
        N = int(input())
    cont = cont+1

    print("Fib(%d) = %d" %(N,Fib[N]))
