print('')
print('Mecânica do Busna')
print('')
print('Seja bem-vindo(a)')
print('')
name = str(input('Digite seu nome: '))
op = 0
while op != 5:
    print('''Escolha as opções:
[ 1 ] Cadastrar cliente novo
[ 2 ] Cadastrar carro novo
[ 3 ] Visualizar clientes
[ 4 ] Visualizar carros
[ 5 ] Finalizar programa''')
    op = int(input('Digite a opção desejada: '))
    print('')
    if op == 1:
        cln = str(input('Digite o nome do cliente novo: '))
        print('')
        print('{} cadastrou o cliente {}'.format(name, cln))
        print('')
    elif op == 2:
        cn = str(input('Digite o carro novo: '))
        print('')
        print('{} cadastrou o carro {}'.format(name, cn))
        print('')
    elif op == 3:
        print('Cliente cadastrado abaixo:')
        print(cln)
        print('')
    elif op == 4:
        print('Carro cadastrado abaixo:')
        print(cn)
        print('')
    elif op == 5:
        print('Finalizando...')
        print('')
    else:
        print('Opção inválida, Tente novamente')
        print('')
print('Programa finalizado!!')
