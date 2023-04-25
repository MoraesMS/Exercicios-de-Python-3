def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


num1 = leiaInt('Digite um valor Inteiro: ')
num2 = leiaFloat('Digite um valor Real: ')
print(f'O valor digitado foi Inteiro foi {num}, e o valor Real foi {num2}.')
