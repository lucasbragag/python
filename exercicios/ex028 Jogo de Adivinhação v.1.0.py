from random import randint
from time import sleep
print('-=-'*19)
print('Jogo de Adivinhação v.1.0')
print('-=-'*19)
print('Neste jogo você irá tentar adivinhar um número de 0 a 5.')
print('Use sua sorte ao seu favor!')
num = int(input('Digite um número de 0 a 5:'))
print('Boa sorte')
print('Carregando........')
n = randint(0, 5)
sleep(2)
if n == num:
    print('Parabéns, você acertou o número.')
else:
    print('Você perdeu, o número aleatório foi {}'.format(n))
print('------------FIM------------')
