sexo = str(input('Informe seu sexo [F / M]: ')).upper().strip()
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [F / M]: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso.')
