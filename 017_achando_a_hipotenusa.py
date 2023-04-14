#forma matemática de se fazer
'''catetoo = float(input('Comprimento do cateto oposto: '))
catetoa = float(input('Comprimento do cateto adjacente: '))
hipotenusa = ((catetoo ** 2) + (catetoa ** 2)) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}.')'''
#utilizando importação
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(co, ca):.f2}')
