while True:
    try:
        N = int(input())
        while N<1001 or N>9999:
            N = int(input())
        senha = N-1
        print(senha)
    except EOFError:
        break
