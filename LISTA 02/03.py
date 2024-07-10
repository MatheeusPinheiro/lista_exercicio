"""
3. Ler um vetor de 10 elementos inteiros e positivos. Criar um segundo vetor da seguinte forma: 
os elementos de índice par receberão os respectivos elementos divididos por 2; 
os elementos de índice ímpar receberão os respectivos elementos multiplicados por 3. 
Imprima os dois vetores. 
"""

# Importações
import os


lista = []
lista2 = []
novo_numero = 0

for i in range(0, 10):

    num = int(input('Informe um elemento: '))
    
    while num <= 0:
        print('Número não permitido')
        num = int(input('Informe um elemento: '))
        os.system('CLS')

    if num > 0:
        lista.append(num)

    os.system('CLS')


for numero in lista:

    if numero % 2 == 0:
        novo_numero = (numero / 2)
    
    elif numero % 2 != 0:
        novo_numero = (numero * 3)
    
    lista2.append(novo_numero)
        
print(lista)
print(lista2)
