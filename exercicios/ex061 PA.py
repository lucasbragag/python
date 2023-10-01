p = int(input('Digite o primeiro termo:'))
s = int(input('Digite a razão:'))
termo = p
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end=' ')
    termo += s
    cont += 1
print('Fim')
