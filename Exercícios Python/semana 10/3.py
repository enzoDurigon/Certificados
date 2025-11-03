palavra = "americanas"
contagem = {}


for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1


for letra, quantidade in contagem.items():
    if quantidade > 1:
        print(f"Letra {letra} aparece {quantidade} vezes")
    else:  
        print(f"Letra {letra} aparece {quantidade} vez")
