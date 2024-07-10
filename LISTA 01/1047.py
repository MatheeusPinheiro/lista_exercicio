"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
"""

# Recebe a hora e minuto inicial e final do usuário
hora_inicial, min_inicial, hora_final, minuto_final = map(int, input().split())

# Converte a hora inicial e final para minutos
minuto_inicial = (hora_inicial * 60) + min_inicial
minuto_final = (hora_final * 60) + minuto_final

# Calcula a duração em minutos
duracao = minuto_final - minuto_inicial

# Se a duração for negativa, significa que o jogo passou pela meia-noite
if duracao <= 0:
    duracao = 24 * 60 + duracao

# Converte a duração total em horas e minutos
horas = duracao // 60
minutos = duracao % 60

# Imprime a duração do jogo
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')