"""
6. Utilizando vetores, crie um programa que organize uma quantidade qualquer de números 
inteiros fornecidos pelo usuário da seguinte forma: primeiro os números pares em ordem crescente 
e depois os números ímpares em ordem decrescente. 
"""

qtd_numeros = int(input('Informe a quantidade de numeros: '))

numeros_pares = []
numeros_impares = []

for i in range(0, qtd_numeros):
    
    if i % 2 == 0:
        numeros_pares.append(i)
    elif i % 2 != 0:
        numeros_impares.append(i)
        
# print(numeros_impares[::-1])
# print(numeros_pares)

numeros_pares.extend(numeros_impares[::-1])
print(numeros_pares)