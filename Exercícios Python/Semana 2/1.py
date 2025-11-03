segundos = int(input ('digite um valor em segundos: '))
horas = segundos / 3600
minutos = (segundos % 3600) // 60
segundosRestantes = segundos % 60
print('{}s corresponde a {:.0f}h {}m e {}s'.format(segundos, horas, minutos, segundosRestantes))

horas2 = int(input('digite as horas: '))
minutos2 = int(input('digite os minutos: '))
segundos2 = int(input('digite os segundos: '))
horasParaSegundos = (horas2 * 3600)
minutosParaSegundos = (minutos2 * 60)
tempoSegundos = horasParaSegundos + minutosParaSegundos + segundos2
print(f'{horas2}h {minutos2}m {segundos2}s sao {tempoSegundos} segundos')