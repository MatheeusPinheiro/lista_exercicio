"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""

valor = int(input())

print(valor)
print(f'{valor // 100} de R$ 100,00')
valor %= 100
print(f'{valor // 50} de R$ 50,00')
valor %= 50
print(f'{valor // 20} de R$ 20,00')
valor %= 20
print(f'{valor // 10} de R$ 10,00')
valor %= 10
print(f'{valor // 5} de R$ 5,00')
valor %= 5
print(f'{valor // 2} de R$ 2,00')
valor %= 2
print(f'{valor // 1} de R$ 1,00')
valor %= 1
