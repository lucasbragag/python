print('Tabuada v3.0')
print('')
while True:
    n = int(input('Digite um número para ver a tabuada:'))
    if n == 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('Digite 0 para finalizar!')
print('Programa finalizado!')
