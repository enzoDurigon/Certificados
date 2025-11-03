hora = int(input('Digite as horas de agora: '))
minuto = int(input('Digite os minutos de agora: '))



def calcular_valor_minutos(hora, minuto):
    minutosTotais = minuto + hora * 60
    return minutosTotais

minutosFaltantes = 1440 - calcular_valor_minutos(hora, minuto)

print(f'Ja se passaram {calcular_valor_minutos(hora, minuto)} minutos do seu dia')
print(f'Ainda faltam {minutosFaltantes} minutos')


