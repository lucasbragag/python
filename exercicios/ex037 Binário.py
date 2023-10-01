print('-=-'*14)
print('\033[4;97mPrograma para converter um número inteiro\033[m')
print('-=-'*14)
num = int(input('Digite o número inteiro:'))
print('Escolha uma das opções abaixo')
print('[1] converter para binário')
print('[2] converter para octal')
print('[3] converter para hexadecimal')
escolha = int(input('Digite a opção escolhida:'))
if escolha == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente')
