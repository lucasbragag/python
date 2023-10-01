m = 'M'
f = 'F'
s = str(input('Digite seu sexo: [M/F]')).upper()[0].strip()
while s not in 'MmFf':
    s = str(input('Dados inválidos. Digite seu sexo novamente:')).strip().upper()[0]
print('Sexo {} registrado no sistema!'.format(s))
