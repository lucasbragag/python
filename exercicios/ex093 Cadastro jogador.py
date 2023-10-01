jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(1, jogador['partidas']+ 1):
    partidas.append(int(input(f'Quantos gols na {c} partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('='*65)
print(jogador)
print('='*65)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

print('='*65)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
print('')

for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols.')

print('')
print(f'Foi um total de {jogador["total"]} gols')
