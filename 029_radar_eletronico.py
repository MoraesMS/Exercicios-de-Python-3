velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('VOCÊ ULTRAPASSOU O LIMITE DE VEOLCIDADE QUE É DE 80Km/H!!!')
    print(f'Você foi multado em R${(velocidade - 80) * 7}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
