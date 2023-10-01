soma = cont = 0
print('')
while True:
    n = int(input('Digite um número:'))
    print('Para finalizar digite 999')
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foi digitado {cont} números e a soma entre eles é {soma}')
print('Programa encerrado!')
