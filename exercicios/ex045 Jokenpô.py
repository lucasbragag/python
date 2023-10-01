from time import sleep
from random import randint
print('')
print('Jokenpô')
print('')
print('Tente ganhar do computador')
print('')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
op = int(input('Qual é sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
print('-=-'*9)
itens = ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2)
print('O computador jogou {}'.format(itens[c]))
print('O jogador jogou {}'.format(itens[op]))
print('-=-'*9)
if c == 0: #computador jogou Pedra
    if op == 0: #jogador jogou Pedra
        print('Empate!')
    elif op == 1: #jogador jogou Papel
        print('Jogador vence!')
    elif op == 2: #jogador jogou Tesoura
        print('Computador vence!')
    else:
        print('Jogada inválida!')

elif c == 1: #computador jogou Papel
    if op == 0: #jogador jogou Pedra
        print('Computador vence!')
    elif op == 1: #jogador jogou Papel
        print('Empate!')
    elif op == 2: #jogador jogou Tesoura
        print('Jogador vence!')
    else:
        print('Jogada inválida!')

elif c == 2: #computador jogou Tesoura
    if op == 0: #jogador jogou Pedra
        print('Jogador vence!')
    elif op == 1: #jogador jogou Papel
        print('Computador venceu!')
    elif op == 2: #jogador jogou Tesoura
        print('Empate!')
    else:
        print('Jogada inválida!')
