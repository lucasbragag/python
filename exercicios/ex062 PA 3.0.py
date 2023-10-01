print('Gerador de PA')
print('')
p = int(input('Digite o primeiro termo:'))
r = int(input('Digite a sua razão:'))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -'.format(termo), end=' ')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termo mais você quer ver?'))
print('Fim')
print('Progressão finalizada com {} termos!'.format(total))
