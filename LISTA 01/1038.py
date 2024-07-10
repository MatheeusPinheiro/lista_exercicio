"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
"""

produtos = [
	{'codigo': 1, 'sanduiche': 'Cachorro Quente', 'preco': 4.00},
	{'codigo': 2, 'sanduiche': 'X-salada', 'preco': 4.50},
	{'codigo': 3, 'sanduiche': 'X-bacon', 'preco': 5.00},
	{'codigo': 4, 'sanduiche': 'Torrada simples', 'preco': 2.00},
	{'codigo': 5, 'sanduiche': 'Refrigerante', 'preco': 1.50},
]

codigo, quantidade = map(int, input().split())
total = 0

for produto in produtos:
    if produto['codigo'] == codigo:
        total = produto['preco'] * quantidade
        break
    
print(f'TOTAL: R$ {total:.2f}')