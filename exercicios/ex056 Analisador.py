somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('Digite os dados da {} pessoa.'.format(p))
    n = str(input('Digite o nome:')).strip()
    i = int(input('Digite a idade:'))
    s = str(input('Sexo:[M/F]:')).strip()
    print('')
    somaidade += i
    if p == 1 and s in 'Mm':
        maioridadehomem = i
        nomevelho = n
    if s in 'Mm' and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n
    if s in 'Ff' and i < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {} anos.'.format(mediaidade))
print('O homem mais velho é o {} , com {} anos.'.format(nomevelho, maioridadehomem))
print('Tem {} mulheres com menos de 20 anos.'.format(totmulher20))
