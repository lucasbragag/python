soma = 0
cont = 0
print('')
print('Digite 6 números para somar apenas os pares')
for c in range(1, 7):
    n = int(input('Digite o {} valor:'.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números pares, e a soma entre eles é {}'.format(cont, soma))
