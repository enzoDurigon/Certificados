valor = int(input('Digite o valor do saque: '))

if valor < 10 or valor > 600:
    print('o valor precisa ser entre 10 e 600 reais.')
    exit()


notas = [100, 50, 10, 5, 2]


for nota in notas:
    quantidade = valor // nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')
        valor -= quantidade * nota 