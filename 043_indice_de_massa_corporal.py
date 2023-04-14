peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}.')
if imc < 18.5:
    print('Coma mais! Abaixo do peso.')
elif imc < 25:
    print('Parabéns! Peso ideal.')
elif imc < 30:
    print('Fica ligado! Sobrepeso.')
elif imc < 40:
    print('Alerta AMARELO! Obesidade!')
else:
    print('Alerta VERMELHO! Obesidade mórbida!')
