"""
4. Ler um vetor com 10 nomes de pessoas, após pedir que o usuário digite um nome qualquer de pessoa. 
Escrever a mensagem “ACHEI”,
se o nome estiver armazenado no vetor C ou “NÃO ACHEI” caso contrário. 
"""

#Importações
import os

nomes = []

for i in range(0, 10):

   nome = input('Informe um nome: ')
   nomes.append(nome)
   os.system('CLS')


nome_pesquisar = input('Informe o nome que deseja buscar no vetor: ')

if nome_pesquisar in nomes:
    print('ACHEI')
else:
    print('NÃO ACHEI')