from time import sleep
velocidade = float(input('Qual a velocidade em km/h em que o carro passou?'))
if velocidade <= 80:
    print('{:.0f} km/h está dentro do limite.'.format(velocidade))
    print('Tenha um bom dia,dirija com segurança!')
else:
    print('O carro foi multado, pois {:.0f}km/h está acima do limite da via que é 80km/h.'.format(velocidade))
    multa = (velocidade - 80) * 7
    print('Calculando o valor da multa....')
    sleep(2)
    print('A multa ficou R${:.2f}'.format(multa))
