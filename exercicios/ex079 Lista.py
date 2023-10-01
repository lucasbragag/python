lista = []
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor repetido, tente novamente!')
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta in 'N':
        break
lista.sort()
print('Você digitou:', end=' ')
#print(f'Você digitou: {sorted(lista)}', end=' ')
for c in lista:
    print(c, end=' ')
