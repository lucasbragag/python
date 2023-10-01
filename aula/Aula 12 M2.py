name = str(input('Digite seu nome:'))
if name == 'Lucas':
    print('Você tem um nome lindo!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif name in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!!')
else:
    print('Seu nome é bem comum')
print('Tenha um ótimo dia, {}!!'.format(name))
