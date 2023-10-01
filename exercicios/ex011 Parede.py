n1 = float(input('Digite o valor da largura da parede (em metros):'))
n2 = float(input('Digite o valor da altura da parede (em metros):'))
a = n1 * n2
b = a / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m². \nE você precisa de {:.1f} litros de tinta para pintar a parede.'.format(n1, n2, a, b))
