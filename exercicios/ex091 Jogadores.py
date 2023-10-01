from random import randint
from operator import itemgetter
jogadores = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}

ranking = {}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
print('='*30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse= True)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
