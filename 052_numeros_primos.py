num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}\033[m', end=' ')
if tot > 2:
    print(f'\nO número {num} foi divisível {tot} vezes, ele não é primo.')
else:
    print(f'\nO número {num} foi divisível {tot} vezes, ele é primo.')