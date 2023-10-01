from datetime import date
print('')
print('Maioridade')
print('')
ano = date.today().year
tmaior = 0
tmenor = 0
for c in range(1, 8):
    n = int(input('Digite o ano de nascimento da {} pessoa:'.format(c)))
    i = ano - n
    if i >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(tmaior))
print('E {} pessoas menores de idade.'.format(tmenor))
