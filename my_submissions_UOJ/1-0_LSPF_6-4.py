soma = 0
cont = 0
for i in range(6):
    N = float(input())
    if N>0:
        soma = soma + N
        cont = cont + 1
    else:
        continue
media = soma/cont
print(str(cont)+' valores positivos')
print(str(round(media,1)))
