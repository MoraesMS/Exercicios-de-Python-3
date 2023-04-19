galera = []
pessoa = {}
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas "F" ou "M".')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) #para fazer cópia de um dicionário para dentro de uma lista, se usa esse comando
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas "S" ou "N".')
    if resp == 'N':
        break
print('-=-' * 15)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'"{p["nome"]}" ', end='')
print('\nD) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= média:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('\n>>> Programa Encerrado! <<<')
