lista = [] # Lista
menor = maior = 0  # Menor e maior
for c in range(0, 5): # Repetição de 0 a 5
    lista.append(int(input('Digite um número:'))) # Adicionando um número a lista
    if c == 0: # Se o contador for 0
        maior = menor = lista[c]  # O valor vai ser maior e menor
    else:  # Se não
        if lista[c] > maior: # Se a lista na posição c for maior
            maior = lista[c] # Passa a ser o maior
            if lista[c] < menor: # Se a lista na posição for menor
                menor = lista[c] # Passa a ser menor
print('Os número digitados foram:', end=' ') # Mostrando o print
for c in lista: # Formatando os números
    print(c, end=' ') # Mostrando os números
print('.')
print(f'\nO maior número da lista foi o {maior} na posição', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(i+1, end='...')
print('!')
print(f'\nO menor número da lista foi o {menor} na posição', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(i+1, end='...')
print('!')
