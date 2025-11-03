continuar = 'sim'
preco = 0
produto = 0



while continuar == 'sim':
    continuar2 = 'sim'

    while continuar2 == 'sim':   
        produto += int(input('Digite a quantidade do produto: '))
        preco += int(input('Digite o preco do produto: '))
        continuar2 = str(input('Deseja digitar mais algum produto? ')).lower()
    
    if produto >= 2 and produto <= 4:
        descontoPreco = (preco / 100) * 5 
        descontoPorcemtagem = 5
    elif produto <= 7:
        descontoPreco = (preco / 100) * 10 
        descontoPorcemtagem = 10
    elif produto > 7:
        descontoPreco = (preco / 100) * 15
        descontoPorcemtagem = 15
    else: 
        descontoPreco = 0
        descontoPorcemtagem = 0

    precoApagarComDesconto = preco - descontoPreco
    precoApagarSemDesconto = preco

    print(f'Valor total da compra sem desconto: R$ {precoApagarSemDesconto}')
    print(f'Valor porcentual de desconto: {descontoPorcemtagem}%')
    print(f'Valor do desconto: R$ {descontoPreco:.2f}')
    print(f'Valor a pagar com desconto: R$ {precoApagarComDesconto}')

    
    continuar = str(input('Tem outro cliente?: ')).lower()




    
    