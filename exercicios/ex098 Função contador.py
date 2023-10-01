from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if f == 0:
        f - 2
    for c in range(i, f+1, p):
        print(f'{c}', end=' ')
        #sleep(0.5)
    print('Fim')


# Programa principal
print('-='*20)
contador(1, 10, 1)
print('-='*20)
contador(10, 0, -2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
contador(i= int(input('Início: ')), f= int(input('Fim: ')), p= abs(int(input('Passo: '))))