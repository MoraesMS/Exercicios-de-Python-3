from datetime import datetime
funcionário = {}
funcionário['nome'] = str(input('Nome: ')).strip().title()
anonsc = int(input('Ano de Nascimento: '))
funcionário['idade'] = datetime.now().year - anonsc
funcionário['ctps'] = int(input('Carteria de trabalho [0 não tem]: '))
if funcionário['ctps'] != 0:
    funcionário['contratação'] = int(input('Ano de contração: '))
    funcionário['salário'] = float(input('Salário: R$'))
    funcionário['aposentadoria'] = funcionário['idade'] + ((funcionário['contratação'] + 35) - datetime.now().year)
print('-=-' * 10)
for k, v in funcionário.items():
    print(f' - {k} tem o valor {v}.')