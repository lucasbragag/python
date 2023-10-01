pessoas = [] # Lista de pessoas
temp = [] # Lista temporária
maior = menor = 0
while True:
    temp.append(str(input('Nome:')).strip().title())
    temp.append(float(input('Peso:')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso é de {maior}kg, Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso é de {menor}kg, Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
