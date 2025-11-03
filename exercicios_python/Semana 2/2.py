import math
valor = int(input("digite o valor da lata de tinta: "))
largura = float(input('digite a largura do terreno: '))
comprimento = float(input('digite o comprimento do terreno: '))
area = (largura * comprimento)
lata =  15
latasNecessarias = math.ceil(area / lata)
valorLata = (latasNecessarias * valor)
print (f"voce precisara de {latasNecessarias} latas e voce pagara {valorLata} reais pelas latas")