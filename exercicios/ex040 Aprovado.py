print('\033[4;97mCalcule a média entre duas notas\033[m')
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
if m < 5.0:
    print('Sua média foi {}'.format(m))
    print('Você foi reprovado, sua média ficou abaixo de 5.0')
elif m < 6.9:
    print('Sua média foi {}'.format(m))
    print('Você está em recuperação.')
else:
    print('Sua média foi {}'.format(m))
    print('Parabéns, você foi aprovado(a).')
