vendasPorVendedor = []
faixasSalariais = [0] * 9

while True:
    vendasPorVendedor.append(int(input('Digite as vendas em R$ de cada um dos vendedores: ')))
    continuar = str(input('Deseja Digitar outro vendedor?: ')).lower
    if continuar == 'nao':
        break
    break


for vendas in vendasPorVendedor:
    salario = 200 + (0.09 * vendas)

if salario >= 1000:
    faixa = 8
else:
    faixa = (int(salario) - 200) // 100

faixasSalariais[faixa] += 1

faixas = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
    "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 ou mais"]

for i, contador in enumerate():
    print(f"Vendedores na faixa {faixas[i]}: {contador}")