from math import sqrt, floor
n = int(input('Digite um número:'))
raiz = sqrt(n)
#print('A raiz quadrada de {} é {}.'.format(n, math.floor(raiz)))
print('A raiz quadrada de {} é {:.2f}.'.format(n, floor(raiz)))
