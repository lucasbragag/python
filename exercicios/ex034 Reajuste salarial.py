salário = float(input('Digite o salário do funcionário:R$'))
if salário <= 1250:
    a = (salário * 15) / 100
    print('Seu salário aumentou R${} , então seu valor reajustado ficou R${}'.format(a, (salário + a)))
else:
    a = (salário * 10) / 100
    print('Seu salário aumentou R${} , então seu valor reajustado ficou R${}'.format(a, (salário + a)))
