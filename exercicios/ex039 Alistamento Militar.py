from datetime import date
print('Alistamento Militar')
ano = int(input('Digite o ano de nascimento:'))
a = date.today().year # ano atual
i = a - ano  #idade do usuário
q = 18 - i # quantos anos faltam
j = i - 18
if i < 18: # se o usuário tem menos de 18 anos
    print('Você tem {} anos e ainda não chegou a hora do alistamento'.format(i))
    print('Mas está chegando, faltam {} anos.'.format(q))
    print('Seu alistamento será em {}'.format(q + a))
elif i == 18:
    print('Você tem 18 anos e precisa se alistar.')
elif i > 18:
    print('Você tem {} anos, já deveria ter se alistado {} anos atrás, em {}'.format(i, j, a - j))
