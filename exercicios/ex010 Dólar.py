n1 = float(input('Digite seu saldo para saber quantos dólares você pode comprar:R$'))
n2 = float(input('Digite o valor do dólar atualmente:US$'))
#n3 = float(3.27)
a = n1 / n2
#b = n1 / n3
print('Seu saldo em reais é R${} e você pode ter US${:.2f} dólares'.format(n1, a))
