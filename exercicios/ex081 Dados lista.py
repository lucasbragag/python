lista = list()
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if 'N' in resposta:
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} números.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 tem na lista.')
else:
    print('O valor 5 não tem na lista.')
