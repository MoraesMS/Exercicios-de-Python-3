princ = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        princ[0].append(num)
    else:
        princ[1].append(num)
print('=-=' * 15)
princ[0].sort()
princ[1].sort()
print(f'Os valores pares digitados foram {princ[0]}.')
print(f'Os valores ímpares digitados foram {princ[1]}.')
