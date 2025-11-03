import time
from colorama import Fore, Style, Back

minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
    

totalSegundos = minutos * 60 + segundos


for segundosREstantes in range(totalSegundos, 0, -1):
    mins = segundosREstantes // 60
    secs = segundosREstantes % 60
    timer = f'{mins:02}:{secs:02}'

    if segundosREstantes <= 10:
        print(timer + Fore.RED)
    else:
        print(timer)
    time.sleep(1)
print('FIM')