def fatorial(n, show = False):
    '''
    -> Calcula o Fatorial de um número
    :param n: o número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: o valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
n = int(input('Você deseja ver o FATORIAL de qual número? '))
print((fatorial(n, show = True)))