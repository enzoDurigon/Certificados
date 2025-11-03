numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
numero3 = int(input('digite o terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print('o numero 1 e o maior.')
elif numero2 > numero1 and numero2 > numero3:
    print('o numero 2 e o maior')
elif numero3 > numero1 and numero3 > numero2:
    print('o numero 3 e o maior.')


if numero1 < numero2 and numero1 < numero3:
    print('o numero 1 e o menor.')
elif numero2 < numero1 and numero2 < numero3:
    print('o numero 2 e o menor.')
elif numero3 < numero1 and numero3 < numero2:
    print('o numero 3 e o menor.')


numero = [numero1, numero2, numero3]
numero.sort()  
print(f"Os numeros em ordem crescente sao: {numero}")