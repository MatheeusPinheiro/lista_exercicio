"""
7. Dados dois vetores de tamanho N, faça uma função que diga se os mesmos possuem conteúdo igual.
"""

vetor1 = [1,2,3,4,5,4]
vetor2 = [1,2,3,4,5,6]


def conteudo_vetor(lista, lista2):
    
    for i in range(len(lista)):
        if lista[i] != lista2[i]:
            return False
    
    return True
    


print(conteudo_vetor(vetor1,vetor2))