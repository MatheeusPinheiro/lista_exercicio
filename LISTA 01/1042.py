"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

"""

lista = []
n1,n2,n3 = map(int, input().split())

lista.append(n1)
lista.append(n2)
lista.append(n3)

lista_aux = lista.copy()
lista_aux.sort()
for num in lista_aux:
    print(num)
    
print()

for num in lista:
    print(num)

