""""
2. Ler um vetor de 10 elementos. Crie um segundo vetor, com todos os elementos na ordem inversa, 
ou seja, o último elemento passará a ser o primeiro, 
o penúltimo será o segundo e assim por diante. Imprima os dois vetores. 
"""

#Importações
import os


lista = []
lista2 = []

for i in range(0,10):
    num = input('Informe um elemento: ')
    lista.append(num)
    os.system('CLS')
    
lista2 = lista[::-1].copy()
print(lista)
print(lista2)
