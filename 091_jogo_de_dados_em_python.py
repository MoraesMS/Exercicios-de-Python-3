from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
for j in range(1, 5):
    jogadores[f'jogador {j}'] = randint(1, 6)
ranking = []
print('-=-' * 9)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# O que você vai colocar de argumento no sorted é o seguinte:
# sorted(nome_do_dicionario.items(), key=lambda item: item[1], reverse=True))
# O `key=lambda item: item[1]' faz com o sort seja feito a partir dos valores que os jogadores obtiveram.
# Se quiser fazer com as chaves ao invés dos valores, use item[0]. Assim não precisar importar e fazer uso do itemgetter.
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=-' * 9)
print('  >> RANKING DOS JOGADORES <<')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
