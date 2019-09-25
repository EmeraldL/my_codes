while True:
    X = int(input())
    if X==0:
        break
    resp = []
    for i in range(1,X+1,1):
        resp.append(i)
    print(" ".join(map(str, resp)))
