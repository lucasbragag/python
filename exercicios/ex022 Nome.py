frase = str(input('Digite seu nome completo:')).strip()
print('Seu nome completo é {}'.format(frase))
print('Seu nome maiúsculo:{}'.format(frase.upper()))
print('Seu nome minúsculo:{}'.format(frase.lower()))
print('Seu nome tem {} letras'.format(len(frase)-frase.count(' ')))
s = frase.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(s[0], len(s[0])))
