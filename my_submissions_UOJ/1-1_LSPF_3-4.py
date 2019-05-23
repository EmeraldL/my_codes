X = int(input())

while X<1 or X>4:
    X = int(input())
    
alcool = 0
gasolina = 0
diesel = 0

while X != 4:
    if X == 1:
        alcool = alcool+1

    elif X == 2:
        gasolina = gasolina+1

    elif X == 3:
        diesel = diesel+1

    X = int(input())

    while X<1 or X>4:
        X = int(input())

print("MUITO OBRIGADO")
print("Alcool: "+str(alcool))
print("Gasolina: "+str(gasolina))
print("Diesel: "+str(diesel))
