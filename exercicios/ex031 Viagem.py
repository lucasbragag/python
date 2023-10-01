print('Calcule o custo da sua viagem')
d = float(input('Digite em km a distância da sua viagem:'))
if d <= 200.0:
    p = d * 0.50
    print('Sua viagem de {}km irá custar R${}'.format(d, p))
else:
    p = d * 0.45
    print('Sua viagem de {}km irá custar R${}'.format(d, p))
#preço = distância * 0.50 if distância <= 200 else distancia * 0.45
