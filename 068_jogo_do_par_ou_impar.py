from random import randint
print('=-= JOGO DO PAR OU ÍMPAR =-=')
print('=' * 28)
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    parimpar = computador + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P / I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {parimpar} ', end='')
    print('Deu PAR!' if parimpar % 2 == 0 else 'Deu ÍMPAR!')
    if escolha in 'P' and parimpar % 2 == 0 or escolha in "I" and parimpar % 2 == 1:
        print('Você venceu!')
        cont += 1
    else:
        print('Computador venceu!')
        break
    print('Vmaos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
