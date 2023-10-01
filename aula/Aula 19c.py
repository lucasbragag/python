pessoas = {'nome': 'Lucas', 'idade': 23, 'sexo': 'Masculino'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é {pessoas["sexo"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
print(pessoas)