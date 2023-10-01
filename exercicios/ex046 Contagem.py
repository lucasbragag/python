from time import sleep
print('')
print('\033[4;97mContagem regressiva para o ano novo\033[m')
print('')
op = str(input('Digite \033[4;97mSIM\033[m para começar:')).upper()
if op == 'SIM':
    sleep(1)
    print('Vai começar...')
    sleep(1)
    for c in range(10, -1, -1):
        sleep(1)
        print(c)
    print('\033[4;97mFeliz Ano Novo!!!\033[m')
else:
    print('\033[4;31mTente novamente\033[m, digite a palavra \033[4;97mSIM\033[m')
