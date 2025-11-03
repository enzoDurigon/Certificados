import random

saldo = 100
aposta = 0
print('SE A SOMA FOR 7 OU 11, VOCE GANHA O DOBRO DO VALOR APOSTADO')

while saldo > 0:
    print(f'SALDO DISPONIVEL: {saldo}')
    aposta = int(input('Digite sua aposta: '))

    if aposta > saldo:
        print('saldo invalido')
        break
    elif aposta < 0:
        print('A aposta nao pode ser menor que 0')
        break
    
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma = dado1 + dado2 
    print(f'A soma dos dados foi: {soma}')

    if soma == 7 or soma == 11:
        saldo += aposta * 2
    else:
        saldo -= 20