from random import randint
print('-'*15)
print('Par ou Ímpar')
print('-'*15)
s = randint(0, 10)
v = 0
while True:
    u = int(input('Digite um número:'))
    total = u + s
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Impar?')).strip().upper()[0]
    print(f'Você jogou {u} , o computador {s} e a soma entre eles é {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu Ímpar')
    if op == 'P':
        if total % 2 == 0:
            print('O jogador venceu!!')
            v += 1
        else:
            print('O computador venceu!')
            break
    elif op == 'I':
        if total % 2 == 1:
            print('O jogador venceu!!')
            v += 1
        else:
            print('O computador venceu!')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Você vendeu {v} vezes')
print('Jogo finalizado!!')
