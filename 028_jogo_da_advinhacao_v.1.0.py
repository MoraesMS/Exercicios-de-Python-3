from random import randint
print('~' * 30)
print('Vou pensar em um número entre 0 e 5, tente advinhar!')
print('~' * 30)
numc = randint(0, 5)
numj = int(input('Em que número eu pensei? '))
if numc == numj:
    print('Voce acertou!!!')
else:
    print(f'Você errou, eu pensei no número {numc}.')
