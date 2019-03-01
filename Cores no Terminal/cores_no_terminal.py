#! / usr / bin / python
#-*- coding: utf-8 -*-

'''
Este código mostra como deixar os textos coloridos na saída do terminal.
Fiz os teste usando os terminais: Xterm e o Tilix. Além disso testei no Atom. Minha versão do Python é 3.6.1.
.::.
Por: Larissa Samara Paula de França
Porto Velho - Rondônia - Brasil
01/03/2019
.::.
'''

print('\n')
print ('Início aqui! OBS: Talvez você não veja a cor preta antes da vermelha.')

print ('\033[30mIsto é preto')
print ('\033[31mIsto é vermelho')
print ('\033[32mIsto é verde')
print ('\033[33mIsto é amarelo/laranja') #Dependendo terminal, a cor fica com tom mais laranja que amarelo.
print ('\033[34mIsto é azul')
print ('\033[35mIsto é magenta/roxo') #Dependendo terminal, a cor fica com tom mais roxo que magenta.
print ('\033[36mIsto é cyano')
print ('\033[37mIsto é cinza claro')

#Repare que a sintaxe também pode ser usando o +.
print ('\033[90m'+'Aqui temos a cor cinza escuro')
print ('\033[91m'+'Aqui temos a cor vermelho claro')
print ('\033[92m'+'Aqui temos a cor verde claro')
print ('\033[93m'+'Aqui temos a cor amarelo claro')
print ('\033[94m'+'Aqui temos a cor azul claro')
print ('\033[95m'+'Aqui temos a cor magenta claro')
print ('\033[96m'+'Aqui temos a cor cyano claro')
print ('\033[97m'+'Aqui temos a cor branca')

print ('\033[0m') #reset de cores - O terminal volta ao padrão.

#Repare que aqui uso " " ao invés de ' '. Também funciona!
print ("\033[;1m"+"Aqui tudo está em negrito")
print("\n")
print ("\033[;7m"+"Aqui o texto está invertido")
print ("\033[91;7m"+"Também é possível inverter com cores") #Vermelho Escuro.
print ("\033[33;7m"+"Também é possível inverter com cores") #Amarelo/Laranja Claro.
print ("\033[93;7m"+"Também é possível inverter com cores") #Amarelo Escuro.
print ("\033[92;7m"+"Também é possível inverter com cores") #Verde Claro.
print ("\033[94;7m"+"Também é possível inverter com cores") #Azul Claro.
print ("\033[34;7m"+"Também é possível inverter com cores") #Azul Escuro.
print ("\033[95;7m"+"Também é possível inverter com cores") #Magenta Claro.
print ("\033[0m") #reset de cores