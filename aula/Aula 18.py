teste = list()
teste.append('Lucas')
teste.append(23)
galera = list()
galera.append(teste[:])
teste[0] = 'Bruna'
teste[1] = 15
galera.append(teste[:])
print(galera)
