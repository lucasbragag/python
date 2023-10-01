def area(l, c):
    print('-'*20)
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a} m2.')


#Programa principal
print('Controle de Terrenos')
print('-'*20)
area(l= float(input('Largura (m):')), c= float(input('Comprimento (m):')))

