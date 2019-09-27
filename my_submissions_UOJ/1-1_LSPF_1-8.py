while True:
    N1 = float(input())
    while N1>10 or N1<0:
        print("nota invalida")
        N1 = float(input())

    N2 = float(input())
    while N2>10 or N2<0:
        print("nota invalida")
        N2 = float(input())

    media = (N1+N2)/2
    print("media = %.2f" % media)
    X = int(input("novo calculo (1-sim 2-nao)\n"))
    while X>2 or X<1:
        X = int(input("novo calculo (1-sim 2-nao)\n"))
    if X==2:
        break
    else:
        continue
