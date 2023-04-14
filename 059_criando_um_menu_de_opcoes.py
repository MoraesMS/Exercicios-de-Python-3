from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
resp = 0
while resp != 5:
    print('[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGRAMA')
    resp = int(input('>>> Qual é sua opção? '))
    if resp == 1:
        print('=-=' * 10)
        print(f'A soma entre {num1} e {num2} é {num1 + num2}.')
        print('=-=' * 10)
    elif resp == 2:
        print('=-=' * 10)
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}.')
        print('=-=' * 10)
    elif resp == 3:
        if num1 > num2:
            print('=-=' * 10)
            print(f'O maior número é {num1}.')
            print('=-=' * 10)
        else:
            print('=-=' * 10)
            print(f'O maior número é {num2}.')
            print('=-=' * 10)
    elif resp == 4:
        print('=-=' * 10)
        print('Informe os números novamente!')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif resp == 5:
        print('=-=' * 10)
        print('Finalizando...')
        sleep(1.5)
        print('=-=' * 10)
    else:
        print('=-=' * 10)
        print('Opção inválida. Tente novamente.')
        print('=-=' * 10)
print('Fim do programa! Volte Sempre!')
print('=-=' * 10)