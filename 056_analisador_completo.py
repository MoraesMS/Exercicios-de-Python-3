mediaidade = maisvelho = mulhernova = 0
nomemaisvelho = ''
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    mediaidade += idade
    if sexo == 'Mm':
         maisvelho = idade
         nomemaisvelho = nome
    else:
        if idade > maisvelho:
            maisvelho = idade
            nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhernova += 1
print(f'A média de idade do grupo é de {mediaidade / 4} anos.')
print(f'O homem mais velho tem {maisvelho} anos e se chama {nomemaisvelho}.')
print(f'Ao todo são {mulhernova} mulheres com menos de 20 anos.')