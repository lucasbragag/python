from random import randint
s = randint(0, 10)
print('Sou o computador')
print('')
print('Pensei em um número de 0 a 10')
print('')
acertou = False
palpites = 0
while not acertou:
    n = int(input('Digite um número :'))
    print('')
    palpites += 1
    if n == s:
        acertou = True
    elif n != s:
        print('Você errou, tente novamente')
        if n < s:
            print('Seu número é menor')
        elif n > s:
            print('Seu número é maior')
print('Parabéns, você acertou. O número sorteado foi {}'.format(s))
print('Você tentou {}x até conseguir'.format(palpites))
