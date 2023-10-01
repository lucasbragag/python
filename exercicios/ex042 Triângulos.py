print('Analisando Triângulos')
s1 = float(input('Digite o primeiro segmento:'))
s2 = float(input('Digite o segundo segmento:'))
s3 = float(input('Digite o terceiro segmento:'))
# Para formar um triângulo, a soma de duas retas precisa ser menor que a outra
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
    print('Os segmentos acima podem formar um triângulo', end=' ')
    if s1 == s2 == s3:
        print('equilátero')
    elif s1 != s2 != s3 != s1:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Os segmentos acima não pode formar um triângulo.')
