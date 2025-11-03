velocidadeMaxima = float(input('digite a velocidade maxima permitida na via: '))
velocidade = float(input('digite sua velocidade: '))



if velocidade <= velocidadeMaxima:
    print('velocidade dentro do permitido.')
elif velocidade <= velocidadeMaxima * 1.2:
    print('Multa de R$ 130,00.')
elif velocidade <= velocidadeMaxima * 1.5:
    print('Multa de R$ 200,00.')
elif velocidade > velocidadeMaxima * 1.5:
    print('Multa de R$ 500,00 e habilitação suspensa.')