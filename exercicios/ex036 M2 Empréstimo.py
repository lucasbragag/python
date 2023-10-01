print('-=-'*8)
print('\033[4;97mSimulação de empréstimo\033[m')
print('-=-'*8)
valor = float(input('Digite o valor do empréstimo:R$'))
salario = float(input('Digite o valor do seu salário:R$'))
anos = int(input('Em quantos anos você quer pagar?'))
ano = valor / anos
mensal = ano / 12
if mensal > ((salario * 30) / 100):
    print('Infelizmente seu empréstimo foi \033[4;31mnegado\033[m,devido parcela de {:.2f} ser superior a 30% do seu salário.'.format(mensal))
else:
    print('Seu empréstimo foi \033[4;32maprovado\033[m!!! \033[4;32mParabéns\033[m')
    print('O empréstimo de R${} em {} anos com salário de R${}, ficou com uma parcela mensal de R${:.2f}.'.format(valor, anos, salario, mensal))
