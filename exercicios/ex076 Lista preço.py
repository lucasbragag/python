listagem = ('Lápis', 1.80,
            'Borracha', 2.00,
            'Caderno', 15.00,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 10.00,
            'Mochila', 120.32,
            'Caneta', 12.00,
            'Livro', 32.90)
print('-'*45)
print(f'{"Listagem dos produtos":^40}')
print('-'*45)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')




#print('-'*50)
#print('Listagem de preços')
#print('-'*50)
#print('''Lápis....................R$   1.75
#Borracha.................R$   2.00
#Caderno..................R$  15.00
#Estojo...................R$  25.00
#Transferidor.............R$   4.20
#Compasso.................R$   9.99
#Mochila..................R$ 120.32
#Caneta...................R$  22.30
#Livro....................R$  34.90''')
#print('-'*50)
