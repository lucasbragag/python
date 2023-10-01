print('\033[97m-=-'*6)
print('\033[33mBem vindo ao teste')
print('\033[97m-=-'*6)
name = str(input('Qual seu nome?'))
age = int(input('Qual sua idade?'))
gender = str(input('Seu gênero é Masculino ou Feminino?')).title().strip()
a = name.split()
if gender == 'Feminino':
    print('Bem vinda, {} , tenha um ótimo dia!!'.format(a[0]))
else:
    print('Bem vindo, {} , tenha um ótimo dia!!!'.format(a[0]))
