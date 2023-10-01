times = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras',
         'Bragantino', 'Grêmio', 'Athletico-PR', 'Cuiabá',
         'São Paulo', 'Atlético-MG', 'Cruzeiro', 'Internacional',
         'Fortaleza', 'Corinthians', 'Goiás', 'Bahia', 'Santos',
         'Coritiba', 'Vasco da Gama', 'América-MG')

print('')
print('A lista de times do Brasileirão:')
for t in times:
    print(t)
print('')
print('-'*105)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-'*105)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-'*105)
print(sorted(times))
print('-'*105)
print(f'O Grêmio está na {times.index("Grêmio")+1} posição')
