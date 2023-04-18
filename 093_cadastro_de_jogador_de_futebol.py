jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0, jogos):
    partidas.append(int(input(f'Quantos gols na {p + 1}ª partida: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=-' * 10)
print(jogador)
print('-=-' * 10)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 10)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
for i, v in enumerate(partidas):
    print(f' => Na {i + 1}ª partida, fez {v} gols.')
