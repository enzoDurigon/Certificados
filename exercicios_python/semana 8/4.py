numeroProdutos = int(input('Quantos produtos deseja comprar?: '))
if numeroProdutos <= 0:
    print('O numero de produtos tem que ser maior que 0')

valorCompra = 0

for i in range(0, numeroProdutos):
    preco = int(input('Digite o preco de cada produto: '))
    valorCompra += preco


    
if numeroProdutos == 4:
    desconto = (valorCompra / 100) * 4
    descontoPorcentual = 4
elif numeroProdutos == 5:
    desconto = (valorCompra / 100) * 8
    descontoPorcentual = 8
elif numeroProdutos >= 6:
    desconto = (valorCompra / 100) * 12
    descontoPorcentual = 12
else: 
    desconto = 0
    descontoPorcentual = 0

valorApagar = valorCompra - desconto

print(f'Preco total da compra: R$ {valorCompra}')
print(f'Porcentual do desconto: {descontoPorcentual}%')
print(f'Valor a pagar com desconto: R$ {valorApagar}')