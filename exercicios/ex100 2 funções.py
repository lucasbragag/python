from random import randint
from time import sleep
def sorteia(lista):
    for cont in range(1, 6):
        lista.append(randint(0, 10))
    print(f'Sorteando 5 valores da lista:', end=' ')
    for valor in lista:
        print(f'{valor} ', end='')
    print('Pronto.')


def somaPar(lista):
    somap = 0
    for valor in números:
        if valor % 2 == 0:
            somap += valor
    print(f'Somando os valores pares da lista: {números}, temos {somap} ')

# Programa principal
números = list()
pares = list()
sorteia(números)
somaPar(números)
