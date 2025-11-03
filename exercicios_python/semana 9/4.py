modelos = ['fusca', 'gol', 'uno', 'vectra', 'peugeout']
consumo = [7, 10, 12.5, 9, 14.5]
distancia = 1000
precoGasolina = 2.25
maisEconomico = modelos[consumo.index(max(consumo))]

print("\nConsumo de combustível para percorrer 1000 km:")
for i, modelos in enumerate(modelos):
    litrosNecessarios = distancia / consumo[i]
    custo = litrosNecessarios * precoGasolina
    print(f"{i + 1} --- {modelos} --- {litrosNecessarios:.2f} litros --- R$ {custo:.2f}")
print(f'Mais economico: {maisEconomico}')
