palavra = str(input('Digite a string: ')).lower() .strip()
vogal = palavra.count('a') + palavra.count('e') + palavra.count('i') + palavra.count('o') + palavra.count('u')
invertido = palavra[::-1]

print(f'invertido: {invertido}')
print(f'vogais: {vogal}')
