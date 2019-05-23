C = int(input())

lista_digito = []
iteracao = 0

while iteracao < C:
    entrada = input()
    NM = entrada.split(" ")
    N = int(NM[0])
    M = int(NM[1])

    qtd_digito = 0

    while N<1 and M>100:
        entrada = input()
        NM = entrada.split(" ")
        N = int(NM[0])
        M = int(NM[1])

    potencia = N**M
    potencia_str = str(potencia)
    qtd_digito = (len(potencia_str))
    
    lista_digito.append(qtd_digito)
    iteracao = iteracao+1

for cadaum in lista_digito:
    print(cadaum)
