números = list()
temp = list()
for c in range(1, 8):
    temp.append(int(input(f'Digite o {c} valor:')))
    números.append(temp[:])
    temp.clear()
números.sort()
print('Os valores pares digitados foram:', end=' ')
for n in números:
    if n[0] % 2 == 0:
        print(f'{n}', end=' ')
print('\nOs valores ímpares digitados foram:', end=' ')
for n in números:
    if n[0] % 2 == 1:
        print(n, end=' ')
