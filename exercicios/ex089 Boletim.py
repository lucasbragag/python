dados = []
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Digite novamente, quer continuar?')).strip().upper()[0]
    if resp in 'N':
        break
print('='*30)
print(f'{"No.":<4}{"Nome":^10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:^10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(dados) - 1:
        print(f'Notas de {dados[opc][0]} são : {dados[opc][1]}')
