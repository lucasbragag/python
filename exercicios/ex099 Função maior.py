from time import sleep
def maior(* num):
    print('\nAnalisando os valores passados...')
    if len(num) > 1:
        for valor in num:
            print(f'{valor} ', end='')
            sleep(0.5)
        print(f'\nForam informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi o {max(num)}')
    elif len(num) == 1:
        for valor in num:
            print(f'{valor}')
            print('Foi informado apenas 1 valor')
            print(f'O maior valor é {valor}')
    else:
        print('Não foi informado nenhum valor!')
    print('-='*20)


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
