from math import sqrt
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
ch = sqrt(co ** 2 + ca ** 2)
'''hi = math.hypot(co, ca)'''
print('O comprimento da hipotenusa é {:.2f}'.format(ch))
