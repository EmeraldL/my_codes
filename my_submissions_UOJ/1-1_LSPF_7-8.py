N = []

X = float(input())

for j in range (0,100):
    N.append(X)    
    print("N[%d] = %2.4f" %(j, X))
    X = X/2
