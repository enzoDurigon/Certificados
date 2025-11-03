import random


print('DIFICULDADES: FACIL - MEDIO - DIFICIL')
dificuldade = input('Escolha a dificuldade: ').lower().strip()
tentativas = 1

if dificuldade == "facil":
    numeroAleatorio = random.randint(1, 10)
elif dificuldade == "medio":
    numeroAleatorio = random.randint(1, 50)
elif dificuldade == "dificil":
    numeroAleatorio = random.randint(1, 100)


numeroUser = int(input('Digite um numero: '))

while numeroUser != numeroAleatorio:
    print('Tente outro numero.')
    numeroUser = int(input('Digite um numero: '))
    tentativas += 1
print('NUMERO CERTO!')
print(f'{tentativas} TENTATIVAS ')