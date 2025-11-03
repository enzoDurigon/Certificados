sexo = str(input('Informe seu sexo M/F: ')).lower()

while sexo not in 'MmFf':
    sexo = str(input('Sexo invalido por favor Informe seu sexo M/F: ')).lower()
print('Sexo valido.')