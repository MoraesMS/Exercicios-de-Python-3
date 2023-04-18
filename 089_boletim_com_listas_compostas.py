listatemp = []
while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    média = (n1 + n2) / 2
    listatemp.append([nome, [n1, n2], média])
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=-' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>9}')
print('-' * 26)
for i, a in enumerate(listatemp):
    print(f'{i:<4}{a[0]}{média:>9.1f}')
while True:
    print('-' * 35)
    opc = int(input('Quer ver as nostas de qual aluno? [999 interrompe]: '))
    if opc == 999:
        break
    if opc <= len(listatemp) - 1:
        print(f'As notas de {listatemp[opc][0]} são {listatemp[opc][1]}')
print('<<<<< VOLTE SEMPRE >>>>>')
