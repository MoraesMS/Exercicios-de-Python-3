from datetime import date
anoatual = date.today().year
totv = totn = 0
for c in range(1, 8):
    anonsc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = anoatual - anonsc
    if idade >= 21:
        totv += 1
    else:
        totn += 1
print(f'Ao todo tivemos {totv} pessoas maiores de idade.')
print(f'E também tivemos {totn} pessoas menores de idade.')
