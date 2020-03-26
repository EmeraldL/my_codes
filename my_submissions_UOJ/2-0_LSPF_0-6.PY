T = int(input())
resp = input()

respSplit = resp.split(" ")
A = int(respSplit[0])
B = int(respSplit[1])
C = int(respSplit[2])
D = int(respSplit[3])
E = int(respSplit[4])

while T>4 or A>4 or B>4 or C>4 or D>4 or E>4:
    T = int(input())
    resp = input()

    respSplit = resp.split(" ")
    A = int(respSplit[0])
    B = int(respSplit[1])
    C = int(respSplit[2])
    D = int(respSplit[3])
    E = int(respSplit[4])

soma = 0
for i in range(0,len(respSplit)):
    if int(respSplit[i]) == T:
        soma = soma + 1
    else:
        continue

print(soma)
