tot = 0
tot1000 = 0
menor = 0
cont = 0
barato = ''
print('-'*8)
print('Mercado')
print('-'*8)
while True:
    produto = str(input('Nome do produto:')).strip().title()
    valor = float(input('Preço: R$'))
    cont += 1
    tot += valor
    if valor > 1000:
        tot1000 += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar?')).strip().upper()[0]
    if op == 'N':
        break
print('Fim do Programa.')
print(f'O total da compra foi R${tot:.2f}')
print(f'Tem {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
