print('')
print('Consulte se o número é primo ou não')
print('')
n = int(input('Digite o número:'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[4;33m')
        tot += 1
    else:
        print('\033[m')
    print(c)
print('\033[mO número {} foi divisível por {} vezes'.format(n, tot))
if tot <= 2:
    print('O {} é um número primo'.format(n))
elif tot > 2:
    print('O {} não é primo'.format(n))
