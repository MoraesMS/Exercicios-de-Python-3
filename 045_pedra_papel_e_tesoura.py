from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas Opções:\n'
      '[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print(f'Computador jogou {itens[computador]}.')
print(f'Jogador jogou {itens[jogador]}.')
if computador == 0:
      if jogador == 0:
            print('Empatou!!!')
      elif jogador == 1:
            print('Jogador VENCEU!!!')
      elif jogador == 2:
            print('Computador VENCEU!!!')
      else:
            print('Jogada INVÁLIDA!!!')
if computador == 1:
      if jogador == 0:
            print('Computador VENCEU!!!')
      elif jogador == 1:
            print('EMPATOU!!!')
      elif jogador == 2:
            print('Jogador VENCEU!!!')
      else:
            print('Jogada INVÁLIDA!!!')
if computador == 2:
      if jogador == 0:
            print('Jogador VENVEU!!!')
      elif jogador == 1:
            print('Computador VENCEU!!!')
      elif jogador == 2:
            print('EMPATOU!!!')
      else:
            print('Jogada INVÁLIDA!!!')
