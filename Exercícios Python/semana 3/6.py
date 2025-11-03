import random

acertos = 0 
for x in range(5):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    respostaCerta = a * b

    print(f'Qual é o resultado de {a} x {b}?')
    respostaUsuario = int(input('Resposta: '))

    if respostaUsuario == respostaCerta:
        print('ACERTOU')
        acertos += 1 

print(f'Voce acertou {acertos} de 5 perguntas!')