cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número de 0 a 20:'))
    if 0 <= n <= 20:
        break
    print('Tente novamente.')
print(f'O número por extenso é {cont[n]}')
