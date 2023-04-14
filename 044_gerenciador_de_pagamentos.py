print(f'{" LOJAS MORAES ":=^40}')
preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n'
      '[1] à vista dinheiro/pix\n'
      '[2] à vista cartão\n'
      '[3] 2x no cartão\n'
      '[4] 3x ou mais no cartão')
resp = int(input('Qual é a opção? '))
if resp == 1:
    print(f'Sua Compra de R${preço:.2f} vai custar R${preço - (preço * 10 / 100):.2f} no final.')
elif resp == 2:
    print(f'Sua Compra de R${preço:.2f} vai custar R${preço - (preço * 5 / 100):.2f} no final.')
elif resp == 3:
    print(f'Sua Compra será parcelada em 2X de R${preço / 2:.2f}.')
else:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua Compra será parcelada em {parcelas}X de R${(preço + (preço * 20 /100)) / parcelas:.2f} COM JUROS.')
    print(f'Sua Compra de R${preço:.2f} vai custar R${preço + (preço * 20 / 100):.2f} no final.')
