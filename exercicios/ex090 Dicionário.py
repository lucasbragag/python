dados = {}
dados['Nome'] = str(input('Nome: ')).strip().title()
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))

if dados['Média'] >= 7.0:
    dados['Situação'] = 'Aprovado'
elif dados['Média'] >= 5.0:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Reprovado'

print('='*30)

for k, v in dados.items():
    print(f'-{k} é igual a {v}')

print('')
print(dados.items())
