num = int(input('Digite um número para calcular o seu Fatorial: '))
c = num
f = 1 #quando for para multiplicação limpa, se usa 1 no contador
print(f'Calculando {num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
