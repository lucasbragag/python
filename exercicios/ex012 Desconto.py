n1 = float(input('Digite o valor do produto em R$:'))
n2 = float(input('Digite quantos por cento de desconto %:'))
a = (n2 * n1) / 100
b = n1 - a
print('O desconto é R${:.2f}, o valor total ficou R${:.2f}'.format(a, b))
