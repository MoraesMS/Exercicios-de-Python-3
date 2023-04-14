import math
n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão:\n'
      '[1] converter para BINÁRIO\n'
      '[2] converter para OCTAL\n'
      '[3] converter para HEXADECIMAL')
resp = int(input('Sua opção: '))
if resp == 1:
      print(f'{n} convertido para HEXADECIMAL é igual a {bin(n)[2:]}.')
elif resp == 2:
      print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}.')
elif resp == 3:
      print(f'{n}convertido para HEXADECIMAL é igual a {hex(n)[2:]}.')
