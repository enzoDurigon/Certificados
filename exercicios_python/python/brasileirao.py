times = [ 'Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Sao Paulo', 'Internacional', 'Bahia',
'Cruzeiro', 'Atletico Mineiro', 'Vasco', 'Fluminense', 'Criciuma', 'Gremio', 'Red Bull Bragantino',
'Juventude', 'Vitoria', 'Corinthians', 'CA Paranaense', 'Cuiaba', 'AC goianiense',
]


print(f'Os 5 primeiros colocados sao: {times[0:5]}')
print(f'Os 4 ultimos colocados sao: {times[-4:]}')
print(f'Times em ordem alfabetica sao: {sorted(times)}')
print(f'O Redbull Bragantino esta na {times.index('Red Bull Bragantino') + 1} posicao')