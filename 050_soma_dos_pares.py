soma = cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 0:
    print('Você não informou números pares.')
else:
    print(f'A soma dos {cont} números pares é {soma}.')
