expr = str(input('Digite a expressão:'))
pilha = []
cont1 = 0
cont2 = 0
for símb in expr:
    if símb == '(':
        cont1 += 1
    elif símb == ')':
        cont2 += 1
if cont1 == cont2:
    print('A expressão está correta!')
elif cont1 != cont2:
    print('A expressão está incorreta!')
