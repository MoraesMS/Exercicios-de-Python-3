listanum = []
while True:
    n = int(input('Digite um valor: '))
    if n in listanum:
        print('Valor duplicado! Não vou adicionar')
    else:
        listanum.append(n)
        print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-=' * 10)
listanum.sort()
print(f'Você digitou os valores {listanum}.')
