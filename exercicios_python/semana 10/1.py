dicionario = {
    "Nome": "Ana Maria Braga",
    "Endereco": "Av. Maria Augusta, s/n",
    "OperadoraCelular": "Vivo"
}
valor_buscado = "Maria"
chaves_encontradas = []

for chave, valor in dicionario.items():
    
    if valor_buscado in valor:
        chaves_encontradas.append(chave)

print(f'Chaves encontradas: {chaves_encontradas}')

