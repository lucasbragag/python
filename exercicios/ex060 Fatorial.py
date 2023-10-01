'''from math import factorial
n = int(input('Para calcular o seu fatorial, digite um número:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

n = int(input('Para calcular o seu fatorial, digite um número:'))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f)
