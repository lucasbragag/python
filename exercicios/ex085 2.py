núm = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c} valor:'))
    if n % 2 == 0:
        núm[0].append(n)
    else:
        núm[1].append(n)
núm[0].sort()
núm[1].sort()
print('')
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ìmpares digitados foram: {núm[1]}')
