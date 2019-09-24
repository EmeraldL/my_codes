N1 = float(input())
while (N1<0 or N1>10):
    print("nota invalida")
    N1 = float(input())
           
N2 = float(input())
while (N2<0 or N2>10):
    print("nota invalida")
    N2 = float(input())

media = (N1+N2)/2
print("media = "+str(round(media,2)))
