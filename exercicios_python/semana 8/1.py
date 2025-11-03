valor = int(input('Digite o valor do imovel: '))
investimento = int(input('Digite o valor do investimento mensal: '))
taxa = float(input('Digite a taxa de juros mensal: '))
meses = 0
montante = 0
if valor / 100 > investimento:
    print('Nao viavel para investimento.')
    exit()


for meses in range(1, 4000):
    montante = montante * (1 + taxa) + investimento
    if montante >= valor:
        break



print(f'Faltam {meses} meses')