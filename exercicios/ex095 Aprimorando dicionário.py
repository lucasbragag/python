jogador = dict()
partidas = list()
galera = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, jogador['partidas']+ 1):
        partidas.append(int(input(f'Quantos gols na {c} partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    galera.append(jogador.copy())

    resp = str(input('Quer continuar? ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Erro! Digite sim ou não: ')).strip().upper()[0]
    if resp == 'N':
        break

print('='*65)
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(galera):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('='*65)

while True:
    busca = int(input('Digite o número do jogador que você quer ver (999 para parar): '))
    if busca == 999:
        break
    if busca > len(galera):
        print(f'Erro! Não existe o jogador {busca} ')
    else:
        print(f'Levantamento do jogador {galera[busca]["nome"]}:')
        for i, g in enumerate(galera[busca]['gols']):
            print(f'No partida {i+1} fez {g} gols.')
    print('='*65)
print('Finalizando...')
