from time import sleep
print('\033[4;97mMenu\033[m')
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
op = 0
while op != 5:
    print('')
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    op = int(input('Qual sua opção:'))
    print('')
    if op == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação entre os dois número é igual a {}'.format(n1 * n2))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}'.format(maior))
    elif op == 4:
        print('Informe os número novamente')
        n1 = int(input('Digite o novo número:'))
        n2 = int(input('Digite o novo número:'))
    elif op == 5:
        print('Saindo do programa....')
    else:
        print('\033[31mTente novamente! Opção inválida.\033[m')
    sleep(2)
print('Fim do programa!')
