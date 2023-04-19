def area(l, c):
    total = l * c
    print(f'A área de um terreno {l} x {c} é de {total} m².')


print(f'Controle de Terrenos')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
