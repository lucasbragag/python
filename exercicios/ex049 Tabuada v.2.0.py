print('')
print('Tabuada v.2.0')
print('')
n = int(input('Digite um número para ver sua tabuada:'))
for c in range(1, 11):
    print('{}x{}={}'.format(n, c, n * c))
