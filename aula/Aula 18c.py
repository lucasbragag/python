galera = list()
dados = list()
totmaior = totmenor = 0
for c in range(0, 4):
    dados.append(str(input('Nome:')).strip().title())
    dados.append(int(input('Idade:')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
for p in galera:
    if p[1] >= 18:
        totmaior += 1
    elif p[1] < 18:
        totmenor += 1
if totmaior > 2:
    print(f'Na lista temos {totmaior} pessoas maiores de idade.')
if totmaior < 2:
    print(f'Na lista temos {totmaior} pessoa maior de idade.')
if totmenor > 2:
    print(f'Na lista temos {totmenor} pessoas menores de idade.')
else:
    print(f'Na lista temos {totmenor} pessoa menor de idade.')
