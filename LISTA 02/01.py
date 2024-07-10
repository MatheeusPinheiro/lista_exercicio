"""
1 Faça um programa que lê 10 números inteiros do teclado e armazene em um vetor. 
Ao final imprima o vetor armazenado nos dois sentidos. 
"""

#Importações
import os


lista_numeros = []

for i in range(0,10):
    num = int(input('Informe um número: '))
    lista_numeros.append(num)
    os.system('CLS')
    
    
print(lista_numeros)
print(lista_numeros[::-1])