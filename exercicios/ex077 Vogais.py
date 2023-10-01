palavras = ('Aprender', 'Programar', 'Linguagem', 'Python',
            'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
            'Mercado', 'Programador', 'Futuro')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos', end=' ')
    for letra in palavra.lower():
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\n')
print('Programa finalizado')
