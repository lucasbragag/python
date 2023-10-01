lista = []
pares = []
ímpares = []
while True:
    número = int(input('Digite um número:'))
    lista.append(número)
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if número % 2 == 0:
        pares.append(número)
    if número % 2 == 1:
        ímpares.append(número)
    if resposta in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
