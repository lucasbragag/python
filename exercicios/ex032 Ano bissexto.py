from datetime import date
print('-'*24)
print('Análise de ano bissexto ')
print('-'*24)
print('Para o ano atual digite 0 abaixo.')
ano = int(input('Qual ano você quer analisar?'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))
