distv = float(input('Qual a distância de sua viagem? '))
if distv > 200:
    print(f'Sua viagem vai custar R${distv * 0.50:.2f}.')
else:
    print(f'Preço PROMOCIONAL para viagens acima de 200km!\n'
          f'Sua viagem vai custar R${distv * 0.45:.2f}.')
