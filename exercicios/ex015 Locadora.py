d = int(input('Informe quantos dias o carro ficou alugado:'))
km = float(input('Informe a quilometragem percorrida:'))
c = d * 60
k = km * 0.15
print('O carro foi alugado durante {} dias, e rodou {}km, portanto o valor total ficou R${:.2f}'.format(d, km, (c+k)))
