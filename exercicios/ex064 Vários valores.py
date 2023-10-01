print('-'*27)
print('Programa de vários números')
print('-'*27)
print('Para finalizar o programa digite 999')
n = 0
cont = 0
soma = 0
# n = cont = soma = 0
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print('Você digitou {} números'.format(cont))
print('A soma dos número é {}'.format(soma))
