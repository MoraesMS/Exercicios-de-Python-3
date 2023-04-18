from random import randint
jogadores = {}
for j in range(1, 5):
    jogadores[f'jogador {j}'] = randint(1, 6)
print('-=-' * 15)
for k, v in