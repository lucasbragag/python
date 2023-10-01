print('')
print('10 Termos de uma PA')
print('')
p = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
d = p + (10 - 1) * r #décimo
for c in range(p, d + r, r):
    print(c)
print('Acabou')
