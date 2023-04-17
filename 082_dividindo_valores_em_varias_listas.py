num = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    num.append(n)
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('=-=' * 15)
print(f'A Lista completa é {num}.')
print(f'A lista de pares é {par}.')
print(f'A lista de ímpares é {impar}.')
