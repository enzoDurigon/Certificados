def filtrar_clientes(clientes, idadeMin, idadeMax, localizacao, valorMinimoCompras):
    clientesFiltrados = []
    
    for cliente in clientes:
        nome, idade, cidade, valorCompras = cliente
        if idadeMin <= idade <= idadeMax and cidade == localizacao and valorCompras >= valorMinimoCompras:
            clientesFiltrados.append(cliente)
    return clientesFiltrados


clientes = [
    ("Alice", 30, "São Paulo", 500),
    ("Bob", 25, "Rio de Janeiro", 300),
    ("Carol", 35, "São Paulo", 700),
    ("David", 40, "Brasilia", 1000),
    ("Eva", 28, "Rio de Janeiro", 400),
]

idadeMin = 25
idadeMax = 40
localizacao = "São Paulo"
valorMinimoCompras = 500



clientesFiltrados = filtrar_clientes(clientes, idadeMin, idadeMax, localizacao, valorMinimoCompras)
print(clientesFiltrados)
        
