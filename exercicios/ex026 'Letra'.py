frase = str(input('Digite uma frase:')).strip().lower()
print('Na frase digitada a letra {} aparece {} vezes'.format('A', frase.count('a')))
print('A primeira letra {} apareceu na posição {}'.format('A', frase.find('a')+1))
print('A ultima letra {} apareceu na posição {}'.format('A', frase.rfind('a')+1))
