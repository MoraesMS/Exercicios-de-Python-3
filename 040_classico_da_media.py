n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {media}.')
if media < 5:
    print('REPROVADO! Estude mais!')
elif media < 7:
    print('RECUPERAÇÃO! Ainda da tempo, estude!')
else:
    print('APROVADO!!! Meus Parabéns!!!')
