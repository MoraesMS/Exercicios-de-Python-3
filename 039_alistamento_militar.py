from datetime import date
anonasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
print(f'Quem nasceu em {anonasc} tem {idade} anos em {anoatual}.')
if idade < 18:
    print(f'Ainda falta {18 - idade} ano(s) para o seu alistamento.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {anoatual - (idade - 18)}.')
