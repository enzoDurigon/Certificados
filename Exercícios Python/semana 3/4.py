print('Mercado J&F - Promoção FRIBOI')
print('1- Filé Duplo')
print('2- Alcatra')
print('3- Picanha')
tipo = int(input('Digite o tipo que deseja levar: '))
quantidade = int(input('Digite a quantidade comprada (em KG): '))
print('A compra será realizada no cartão de débito?')
debito = int(input('1- SIM    2- NÃO: '))

if quantidade <= 5:
    preco = {1: 4.90, 2: 5.90, 3: 6.90}
elif quantidade > 5:
    preco = {1: 5.80, 2: 6.80, 3: 7.80}
tipos = {1: "Filé Duplo", 2: "Alcatra", 3: "Picanha"}

carne = tipos[tipo]
precoKg = preco[tipo]

if debito == 1:
    desconto = 0.05
    pagamentoDebito = 'SIM'
else:
    desconto = 0
    pagamentoDebito = 'NÃO'

precoTotal = precoKg * quantidade
valorDesconto = precoTotal * desconto
valorAPagar = precoTotal - valorDesconto

print('*********************************************')
print(f"Tipo de Carne: {carne}")
print(f"Quantidade: {quantidade:.2f} kg")
print(f"Preço Total: R$ {precoTotal:.2f}")
print(f"Pagamento em débito: {pagamentoDebito}")
print(f"Desconto: R$ {valorDesconto:.2f}")
print(f"Valor Total a Pagar: R$ {valorAPagar:.2f}")
print('*********************************************')