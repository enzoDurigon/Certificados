tamanho = int(input("digite o tamanho do arquivo em MB: "))
velocidade = int(input("digite a velocidade da internet em Mbps: "))
tempo = ((tamanho / velocidade) * 8)
rapidez = tempo < 60
print(f"o download de seu arquivo demorara {tempo} segundos")
print(f"download rapido? {rapidez}")