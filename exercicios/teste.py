print('Votação 2022')
candidato1 = 'Bolsonaro'
candidato2 = 'Lula'
n1 = 22
n2 = 13
cont = 0
print('='*31)
print(f'Os candidatos para as eleicões são:')
print(f'{candidato1} com número {n1}')
print(f'{candidato2} com número {n2}')
print('='*31)
while True:
    voto = int(input('Digite o número para votar:'))
    cont += 1
    print('Seu voto foi para Lula!')
    print('')
    if voto == 0:
        break
print(f'O Lula teve um total de  {cont-1} votos')
print('O bolsonaro teve um total de 0 votos')
