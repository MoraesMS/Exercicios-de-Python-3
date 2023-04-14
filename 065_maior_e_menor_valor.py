maiorn = menorn = num = cont = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    num += n
    cont += 1
    if cont == 1:
        maiorn = menorn = n
    else:
        if n > maiorn:
            maiorn = n
        elif n < menorn:
            menorn = n
    resp = str(input('Quer continuar? [S / N]: '))
print(f'Você digitou {cont} números e a média foi {num / cont}.')
print(f'O maior valor foi {maiorn} e o menor foi {menorn}.')
