sabores = ("Mussarela", "Calabresa", "Frango com Catupiry")
tamanhos = ("Pequena", "Media", "Grande")

while True:
    print('''MENU: 
    1. Escolher o sabor da pizza
    2. Escolher o tamanho da pizza
    3. Adicioonar refrigerante
    4. Finalizar o pedido
    ''')
    opcao = int(input('Digite o numero da opcao: '))

    if opcao == 1:
        print('''Opcao de sabores:
            1. Mussarela
            2. Calabresa
            3. Frango com Catupiry''')
        sabor = int(input("Digite o numero do sabor: "))

    if opcao == 2:
        print('''Opcao de tamanhos: 
              1. Pequena
              2. Media
              3. Grande''')
        tamanho = int(input('Digite o numero do tamanho: '))

    if opcao == 3:
        refrigerante = str(input('Deseja adicionar refrigerante? (sim/nao): ')).lower()
    
    if opcao == 4:
        break



print(f'''RESUMO DO PEDIDO:
Sabor escolhido: {sabores[sabor -1]}
Tamanho escolhido: {tamanhos[tamanho -1]}
Refrigerante adicionado: {refrigerante}''')
