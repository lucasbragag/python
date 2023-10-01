print('')
print('Detector de Palíndromo')
print('')
f = str(input('Digite a frase:')).strip().upper()
p = f.split()
j = ''.join(p)
inverso = ''
# inverso = j[::-1] - Fatiamento, isso substitui o for
for letra in range(len(j) - 1, -1, -1):
    inverso += j[letra]
print('Você digitou a frase {}'.format(f))
print('')
if inverso == j:
    print(j, inverso)
    print('Essa frase \033[4;97mé palíndromo!\033[m')
elif inverso != j:
    print(j, inverso)
    print('Essa frase \033[4;31mnão é palíndromo\033[m')
