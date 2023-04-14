from random import randint
palpites = 0
acertou = False
print('Sou seu computador...')
computador = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?')
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez')
print(f'Acertou com {palpites} tentativas. Parabéns!')
