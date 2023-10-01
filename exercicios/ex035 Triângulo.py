print('-=-'*10)
print('Analisador de Triângulos')
print('-=-'*10)
a = float(input('Digite a primeira reta:'))
b = float(input('Digite a segunda reta:'))
c = float(input('Digite a terceira reta:'))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo')
