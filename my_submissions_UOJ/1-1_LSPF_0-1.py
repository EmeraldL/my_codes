while True:
    MN = input()
    MN = MN.split(" ")
    M = int(MN[0])
    N = int(MN[1])
    if M<=0 or N <= 0:
        break
    if M > N:
        m = N
        n = M
    else:
        m = M
        n = N
    soma = 0
    seq = []
    for i in range(m,n+1):
        seq.append(i)
        soma = soma + i
    print(' '.join(map(str, seq))+" Sum="+str(soma))
