"""
5. Faça um programa que leia e monte dois vetores de números inteiros com 20 números cada.
Depois de montados gere um terceiro vetor formado pela diferença dos dois vetores lidos, um quarto
vetor formado pela soma dos dois vetores lidos e por último um quinto vetor formado pela multiplicação dos dois vetores lidos.
"""

import os

vetor1 = []
vetor2 = []

for i in range(0, 40):

   num = int(input('Informe um número: '))

   if num > 0:

       if i > 0 and i <= 20:
           vetor1.append(num)

           i += 1

       if i > 20 and i <= 40:
            vetor2.append(num)

            i += 1


print('Diferença')
print()
for indice, numero in enumerate(vetor1):
    print(f'{numero} - {vetor2[indice]} = {numero - vetor2[indice]}')
    

print('Soma')
print()
for indice, numero in enumerate(vetor1):
    print(f'{numero} + {vetor2[indice]} = {numero + vetor2[indice]}')
    
print('Multiplicação')
print()
for indice, numero in enumerate(vetor1):
    print(f'{numero} * {vetor2[indice]} = {numero * vetor2[indice]}')