maiorp = menorp = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print(f'O maior peso lido foi de {maiorp:.1f}Kg.')
print(f'O menor peso lido foi de {menorp:.1f}Kg.')
