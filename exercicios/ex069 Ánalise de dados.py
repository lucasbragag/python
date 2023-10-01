tot18 = 0
toth = 0
totm20 = 0
while True:
    print('-'*20)
    print('Cadastre uma pessoa')
    print('-'*20)
    i = int(input('Idade:'))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo:')).strip().upper()[0]
    if i >= 18:          # Total de pessoas com 18 anos ou mais
        tot18 += 1
    if s == 'M':         # Total de homens
        toth += 1
    if s == 'F' and i < 20: # Total de mulheres com menos de 20 anos
        totm20 += 1
    cp = ' '
    while cp not in 'SN':
        cp = str(input('Quer continuar?')).strip().upper()[0]
    if cp == 'N':
        break
print(f'Tem {tot18} pessoas com 18 anos ou mais.')
print(f'Tem {toth} homens cadastrados.')
print(f'Tem {totm20} mulheres com menos de 20 anos.')
print('Programa encerrado!')
