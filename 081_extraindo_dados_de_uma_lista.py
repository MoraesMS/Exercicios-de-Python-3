num = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('=-=' * 20)
num.sort(reverse=True)
print(f'Você digitou {len(num)} elementos.')
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista.')
