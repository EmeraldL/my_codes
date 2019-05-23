'''
Autora: Larissa Samara Paula de França
Contato: larissa.oks@gmail.com
Porto Velho - RO, 23/05/2019.
---------------------------------------

COMPORTAMENTO DE PORTA LÓGICA NAND

'''
#Apresentação do progama.
print("\n\t.::. PORTA LÓGICA NAND .::.")
print(" ")
print("\t          ______")
print("\tSinal A -|      |")
print("\t         | NAND |- Saída S ")
print("\tSinal B -|______|")
print(" ")

#Condição para o programa permanecer em loop.
MENU = 1

#Inicialização das variáveis
A = 0
B = 0
S = 0

#Loop do programa.
while MENU==1:

    #Informações sobre as entradas válidas.
    print("\n\t**************************")
    print("\t1 - Sinal lógico alto")
    print("\t0 - Sinal lógico baixo")
    print("\t**************************\n")
    #Recolhendo a informação.
    A = int(input("Informe o sinal lógico da porta A: "))
    B = int(input("Informe o sinal lógico da porta B: "))

    #Condição para garantir que não haja valores diferentes de 0 e 1.
    while A<0 or A>1 or B<0 or B>1:
        print("========================================")
        print("\n\t!!!!!!!! ATENÇÃO !!!!!!!!!")
        print("\t1 - Sinal lógico alto")
        print("\t0 - Sinal lógico baixo")
        print("\t**************************\n")

        A = int(input("Informe o sinal lógico da porta A: "))
        B = int(input("Informe o sinal lógico da porta B: "))

    #Condições (Tabela Verdade)
    if A==1 and B==1:
        S = 0
    elif A==1 and B==0:
        S = 1
    elif A==0 and B==0:
        S = 1
    elif A==0 and B==1:
        S = 1
    #Exibição do Resultado
    print(" ")
    print("========================================")
    print("\n\t.::.  RESULTADO  .::.")
    print("\t        ______")
    print("\tA = "+str(A)+" -|      |")
    print("\t       | NAND |- S = "+str(S))
    print("\tB = "+str(B)+" -|______|\n")
    print("========================================")
    print(" ")

    #Fazer outra simulação?
    print("\t1 - SIM\n\t0 - NÃO\n\t2 - Exibir Tabela Verdade\n")
    MENU = int(input("Deseja testar outra condição?: "))

    #Condição para que a resposta seja válida.
    while MENU<0 or MENU>2:
        print("\t1 - SIM\n\t0 - NÃO\n\t2 - Exibir Tabela Verdade\n")
        MENU = int(input("Deseja testar outra condição?: "))

    #Exibição da Tabela Verdade.
    if MENU==2:
        print(" ")
        print("========================================")
        print("\n\t..Tabela Verdade..\n")
        print("\t      NAND")
        print("\t _______________")
        print("\t| A | B | Saída |")
        print("\t*****************")
        print("\t| 0 | 0 |   1   |")
        print("\t| 0 | 1 |   1   |")
        print("\t| 1 | 0 |   1   |")
        print("\t| 1 | 1 |   0   |")
        print("\t*****************\n")
        print("========================================")

        MENU = 1
        
#Agradecimento        
print("\n\o/ OBRIGADA POR TESTAR ESTE PROGRAMA \O/")
