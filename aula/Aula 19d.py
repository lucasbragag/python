estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Digite o nome do seu estado:')).strip().title()
    estado['sigla'] = str(input('Digite a sigla do seu estado:')).strip().upper()
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v}')
