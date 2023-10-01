print('')
print(f'{"Mecânica do Busna":^45}')
print('')
print('Bem vindo(a) a mecânica especializada em transmissões.')
cadastro = ' '
usuarios = []
senhas = []
while cadastro not in 'ns':
    cadastro = str(input('Você já tem cadastro com a gente?')).strip().lower()[0]
if cadastro in 's':
    print('Vamos fazer seu login...')
    usuario = str(input('Digite seu usuário:'))
    usuarios.append(usuario)
    senha = int(input('Digite sua senha:'))
    senhas.append(senha)
    print(f'Bem vindo(a) {usuario}!')
elif cadastro in 'n':
    print('Vamos criar um usuário para você...')
    usuario = str(input('Digite um usuário:'))
    usuarios.append(usuario)
    senha = int(input('Digite uma senha:'))
    senhas.append(senha)
    print('Usuário cadastrado com sucesso!')
print('')
op = 0
while op != 5:
    print('''O que você deseja fazer:
[1] Cadastrar cliente novo
[2] Cadastrar carro novo
[3] Visualizar clientes
[4] Vizualizar carros
[5] Sair do programa''')
clientes = []
carros = []
    op = int(input('Digite a opção desejada:'))
    if op == 1:
        cliente = str(input('Digite o nome do cliente novo:')).strip().title()
        clientes.append(cliente)
        print(f'Cliente {cliente} cadastrado com sucesso!')
    elif op == 2:
        carro = str(input('Digite o carro para cadastrar:')).strip().title()
        carros.append(carro)
        print(f'{carro} cadastrado com sucesso!')
    elif op == 3:
        print(f'Clientes cadastrados:{clientes}')
    elif op == 4:
        print(f'Carros cadastrados:{carros}')

print('')
#print(f'Usuários cadastrados:{usuarios}')
#print(f'Senhas cadastradas:{senhas}')
