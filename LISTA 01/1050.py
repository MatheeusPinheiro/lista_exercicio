lista_ddd = [
    {'61': 'Brasilia'},
    {'71': 'Salvador'},
    {'11': 'Sao Paulo'},
    {'21': 'Rio de Janeiro'},
    {'32': 'Juiz de Fora'},
    {'19': 'Campinas'},
    {'27': 'Vitoria'},
    {'31': 'Belo Horizonte'},
]

codigo = int(input())
encontrado = False

for item in lista_ddd:
    for key, value in item.items():
        if int(key) == codigo:
            print(value)
            encontrado = True
            break
        
        if encontrado:
            break

if not encontrado:
    print('DDD nao cadastrado')