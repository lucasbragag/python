import webbrowser
from time import sleep

print('=#='*10)
print('\nPara lhe auxiliar, será aberta automaticamente a tela do Google Maps para você efetuar o cálculo preciso do trajeto percorrido\n')
print('=#='*10)
sleep(1.5)
site = webbrowser.open_new_tab('https://www.google.com.br/maps/')
viagem = float(input('\nDigite a quilometragem percorrida em sua viagem: '))
calculo1 = viagem * 0.50
calculo2 = viagem * 0.45
if viagem <= 200:
 print('Para realizar o trajeto de {:.1f}km\nO valor que você pagará na passagem será de R$ {:.2f}'.format(viagem,calculo1))
else:
 print('Para realizar o trajeto de {:.1f}km\nO valor que você pagará na passagem será de R$ {:.2f}'.format(viagem,calculo2))
 