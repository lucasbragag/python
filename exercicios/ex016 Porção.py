'''from math import floor
num = float(input('Digite um valor:'))
print('O número digitado foi {} e sua porção inteira é {:.0f}'.format(num, (floor(num))))'''
from math import trunc
num = float(input('Digite um valor:'))
print('O número digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))
