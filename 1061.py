
dia1 = int(input().split()[1])
hora1, minuto1, segundo1 = map(int, input().split(':'))
tempo1 = segundo1 + minuto1*60 + hora1*60*60 + dia1*24*60*60


dia2 = int(input().split()[1])
hora2, minuto2, segundo2 = map(int, input().split(':'))
tempo2 = segundo2 + minuto2*60 + hora2*60*60 + dia2*24*60*60

diferenca = tempo2 - tempo1

dia = diferenca//(24*60*60)
diferenca = diferenca % (24*60*60)

hora = diferenca//(60*60)
diferenca = diferenca % (60*60)

minuto = diferenca//(60)
diferenca = diferenca % (60)

segundos = diferenca

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundos} segundo(s)')