print('-=-'*6)
print('\033[4;97mCalcule seu IMC\033[m')
print('-=-'*6)
print('')
peso = float(input('Digite seu peso(kg):'))
altura = float(input('Digite sua altura(m):'))
imc = peso / (altura ** 2) #peso divido pela altura ao quadrado
print('De acordo com o seu peso e sua altura, seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Parabéns, você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está na categoria sobrepeso.')
elif 30 <= imc < 40:
    print('Você está na categoria obesidade.')
else:
    print('Você está na categoria obesidade mórbida')
    print('Cuide imediatamente da sua saúde.')
