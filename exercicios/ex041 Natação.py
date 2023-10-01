from datetime import date
print('Confederação Nacional de Natação')
ano = int(input('Digite o ano de nascimento do atleta:'))
a = date.today().year
i = a - ano
print('Você tem {} anos.'.format(i))
if i <= 9:
    print('Portanto irá se classificar na categoria MIRIM.')
elif i <= 14:
    print('Portanto irá se classificar na categoria INFANTIL.')
elif i <= 19:
    print('Portanto irá se classificar na categoria JUNIOR.')
elif i <= 25:
    print('Portanto irá se classificar na categoria SÊNIOR.')
elif i > 25:
    print('Portanto irá se classificar na categoria MASTER.')
