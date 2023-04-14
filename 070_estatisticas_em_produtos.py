print('=' * 30)
print(f'{"LOJÃO SUPER BARATÃO":^30}')
print('=' * 30)
total = mais1000 = menor = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        mais1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    resp = ' '
    while resp not in 'SN':
        print('-' * 30)
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print('-' * 30)
    if resp == 'N':
        break
print('=' * 30)
print(f'{"FIM DO PROGRAMA!":^30}')
print('=' * 30)
print(f'O total da compra foi de R${total:.2f}.')
print(f'Temos {mais1000} produtos custando mais de R$1.000,00.')
print(f'O produto mais barato é "{barato}" que custa R${menor:.2f}.')
