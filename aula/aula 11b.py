nome = input('Digite seu nome:')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto': '\033[30m',
         'branco': '\033[97m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['branco'], nome, cores['limpa']))
