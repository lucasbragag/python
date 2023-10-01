from time import sleep
print('Par ou Ímpar')
sleep(1)
num = int(input('Digite um número:'))
print('Agora vou mostrar se o seu número é par ou ímpar.')
sleep(2)
print('Analisando....')
sleep(1)
r = num % 2    #O num, resto da divisão por 2, 0 ou 1
if r == 0:
    print('Seu número {} é par.'.format(num))
else:
    print('Seu número {} é ímpar.'.format(num))
