print('     ')
print('')
print('{:=^40}'.format(' \033[4;97mMercado Lucas\033[m '))
print('')
print('     ')
produto = float(input('Digite o valor do produto:\033[32mR$\033[m'))
print(' ')
print('Escolha a forma de pagamento')
print('[1] à vista dinheiro')
print('[2] à vista cartão/cheque')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
print('')
pg = int(input('Qual é a opção?'))
print('')
print('O valor normal do produto é \033[32mR${}\033[m'.format(produto))
print('')
if pg == 1: # à vista dinheiro
    d = (produto * 10) / 100
    print('De acordo com a opção 1 , o valor do produto tem \033[4;32m10% de desconto\033[m')
    print('O valor com desconto ficou \033[32mR${}\033[m'.format(produto - d))
elif pg == 2: # à vista no cartão
    d = (produto * 5) / 100
    print('De acordo com a opção 2 , o valor do produto tem \033[4;32m5% de desconto\033[m')
    print('O valor com desconto ficou \033[32mR${}\033[m'.format(produto - d))
elif pg == 3: # Em até 2x no cartão
    print('De acordo com a opção 3 , \033[4;97mnão tem desconto\033[m.')
    pa = int(input('Quantas parcelas?'))
    if pa == 1:
        print('O valor em \033[97m1x\033[m fica \033[32mR${}\033[m'.format(produto))
    elif pa == 2:
        print('Em \033[97m2x\033[m no cartão, a parcela fica \033[32mR${}\033[m'.format(produto / 2))
elif pg == 4:
    j = (produto * 20) / 100
    print('De acordo com a opção 4 , o valor do produto tem \033[4;31m20% de juros\033[m')
    print('O valor com juros fica \033[32mR${}\033[m'.format(produto + j))
    pa = int(input('Quantas parcelas?'))
    print('Em \033[97m{}x\033[m no cartão, a parcela fica \033[32mR${}\033[m'.format(pa, (produto + j) / pa))
else:
    print('\033[4;31mErro , tente novamente!\033[m')
