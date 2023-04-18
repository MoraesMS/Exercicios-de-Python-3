matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:5^}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print('=-=' * 15)
print(f'A soma dos valores pares é {pares}.')
for l in range(0 , 3):
    coluna3 += matriz[l][2]
print(f'A soma da terceira coluna é {coluna3}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é o {maior}.')
