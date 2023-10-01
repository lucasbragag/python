n1 = float(input('Digite seu salário:R$'))
n2 = float(input('Digite quantos por cento de aumento:%'))
a = (n2 * n1) / 100
b = n1 + a
print('Seu salário atual é R${}, com {:.0f}% de aumento ficará R${:.2f} a mais, no total de R${:.2f}'.format(n1, n2, a, b))
