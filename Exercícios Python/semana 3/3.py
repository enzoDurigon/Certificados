from colorama import Fore, init, Style
import random
import datetime


init(autoreset=True)
color = {
    'green': Fore.GREEN,
    'blue': Fore.BLUE,
    'red': Fore.RED,
    }



id = random.randint(1000000, 9999999)
valor = (random.randint(1000, 2000))


cor = color['blue'] if valor >= 1500 else color['red']



print(f'{color["green"]}DADOS DO CLIENTE')
print(Style.BRIGHT + 'NOME:' ' Enzo')
print(Style.BRIGHT + 'AGENCIA:' ' 0001')
print(Style.BRIGHT + 'CONTA CORRENTE:' ' 1234321')
print(f'{color["blue"]}-----------------------------------')


print(f'{color["green"]}DADOS DA TRANSFERENCIA')
print(Style.BRIGHT + 'PARA:' ' Pedro')
print(Style.BRIGHT + 'INSTITUICAO:' ' Picpay')
print(Style.BRIGHT + 'CHAVE:' ' germinaretech@gmail.com')
print(Style.BRIGHT + 'CPF:' ' 341.852.268-88')
print(f'{cor}VALOR: {valor}') 
print(f'{color["blue"]}-----------------------------------')


print(f'{color["green"]}ID/TRANSACAO')
print(Style.BRIGHT + 'ID: ' f'{id}')
print(Style.BRIGHT + f'DATA: {datetime.datetime.now().strftime("%d/%m/%Y")}')
print(f'{color["blue"]}-----------------------------------')