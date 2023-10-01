from random import randint
from time import sleep
num = []
jogos = []
print('-'*30)
print(f'{"Jogo na Mega Sena":^30}')
print('-'*30)
print('O jogo da mega sena é entre 1 e 60.')
quant = int(input('Quantos jogos você quer que eu sorteie?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in num:
            num.append(n)
            cont += 1
        if cont >= 6:
            break
    num.sort()
    jogos.append(num[:])
    num.clear()
    tot += 1
print('='*5, f'Sorteando {quant} jogos', '='*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
