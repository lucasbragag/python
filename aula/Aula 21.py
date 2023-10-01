def contador(i, f, p):
    """
    - Faz uma contagem
    :param i: Inicio
    :param f: Final
    :param p: Passo
    :return: Não possue
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')



contador(2, 10, 1)
