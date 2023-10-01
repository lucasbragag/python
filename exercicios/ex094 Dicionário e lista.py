dados = dict()
galera = list()
soma = média =0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip().title()
    dados['sexo'] = str(input('Sexo: ')).strip().upper()[0]

    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Erro! Por favor, digite M ou F:')).strip().upper()[0]

    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    galera.append(dados.copy())
    resp = str(input('Quer continuar?')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Erro! Digite Sim ou Não:')).strip().upper()[0]

    if resp == 'N':
        break
print('='*50)
print(galera)
print('='*50)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print('\nD) Lista das pessoas acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')

print('\n << Encerrado >>')
