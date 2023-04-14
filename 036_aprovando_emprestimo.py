casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
fin = int(input('Quantos anos de financiamento? '))
prestação = casa / (fin * 12)
minimo = sal * 30 /100
print(f'Para pagar uma casa de R${casa:.2f} em {fin} anos, a prestação será de R${prestação:.2f} por mês.')
if prestação <= minimo:
    print(f'Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')