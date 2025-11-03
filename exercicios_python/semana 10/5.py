estoque = {
    101: "Camiseta",
    102: "Calça",
    103: "Camiseta",
    104: "Sapato",
    105: "Calça"
}


estoque_invertido = {}


for codigo, nome in estoque.items():
    
    if nome in estoque_invertido:
        estoque_invertido[nome].append(codigo)
    else:
        estoque_invertido[nome] = [codigo]

print(estoque_invertido)
