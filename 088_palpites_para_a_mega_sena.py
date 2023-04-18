from random import randint
from time import sleep
lista = []
jogos = []
print('-=' * 7, f' MEGA SENA! ', '=-' * 7)
quant = int(input('Quantos jogos você quer que eu sorteie: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 5, f' Sorteando {quant} jogos! ', '=-' * 52)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 7, f' BOA SORTE! ', '=-' * 7)