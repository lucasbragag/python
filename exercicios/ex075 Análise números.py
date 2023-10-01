num = (int(input('Digite um número:')),
       int(input('Digite outro número:')),
       int(input('Digite mais um número:')),
       int(input('Digite o último número:')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 foi digitado {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na {num.index(3)+1} posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os número pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n},',end=' ')
print('acabou')
