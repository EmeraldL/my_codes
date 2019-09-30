N = int(input())
vec = [0,1]
while True:
    if N==1:
        print(vec[0])
        N = 0
        break
    elif N==2:
        print(' '.join(map(str, vec)))
        N = 0
        break
    else:
        A = N-2
        while N>1:
            for i in range(A):
                fib = vec[i] + vec[i+1] 
                vec.append(fib)
       
                N = N-2 - 1
        
        print(' '.join(map(str, vec)))
        break
