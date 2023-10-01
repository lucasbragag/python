from datetime import date
trabalhadores = {}

trabalhadores['Nome'] = str(input('Nome: ')).strip().title()
ano = int(input(f'Ano de nascimento de {trabalhadores["Nome"]}: '))
atual = date.today().year
trabalhadores['Idade'] = atual - ano
trabalhadores['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))

if trabalhadores['Carteira'] != 0:
    print('='*35)
    print('Você tem carteira de trabalho.')
    print('='*35)
    trabalhadores['Contratação'] = int(input('Ano de contratação: '))
    trabalhadores['Salário'] = float(input('Salário: R$'))
    apos = trabalhadores['Contratação'] + 35
    trabalhadores['Aposentadoria'] = apos - ano
elif trabalhadores['Carteira'] == 0:
    print('='*35)
    print('Você não tem carteira de trabalho.')
    del trabalhadores['Carteira']

print('='*35)
for k, v in trabalhadores.items():
    print(f'- {k} tem o valor de {v}')
