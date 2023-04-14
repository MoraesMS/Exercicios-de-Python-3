real = float(input('Quanto de dinheiro vc tem na carteira? R$'))
dolar = float(input('Qual a cotação do dolar hoje? R$'))
print(f'Com R${real} reais, vc pode comprar ${real / dolar:.2f}')
