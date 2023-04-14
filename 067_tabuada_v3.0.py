while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    for c in range(0, 11):
        print(f'{n} x {c:2} = {n * c:4}')
    resp = str(input('Quer continuar e ver a tabuada de outro número? [S / N]: '))
    if resp in 'Nn':
        break
print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE!')
