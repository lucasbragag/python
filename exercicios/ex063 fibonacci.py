print('-'*27)
print('Sequência de Fibonacci v1.0')
print('-'*27)
termo = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    cont += 1
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' - Programa finalizado')