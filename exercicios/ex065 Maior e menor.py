print('-'*19)
print('Maior e menor valor')
print('-'*19)
op = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while op in 'Ss':
    n = int(input('Digite um número:'))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print('Você que continuar?')
    op = str(input('[S/N]:')).upper().strip()[0]
print('Você digitou {} números!'.format(cont))
print('A média entre eles foi {:.1f}!'.format(soma / cont))
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))
print('Programada finalizado!!')
