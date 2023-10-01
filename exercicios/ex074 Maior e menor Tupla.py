from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in num:
    print(n, end=' ')
print(f'\nO maior número foi {max(num)}')
print(f'O menor número foi {min(num)}')
