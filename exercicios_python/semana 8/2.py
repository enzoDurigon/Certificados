idadeMaior = 0
idadeMenor = 100
idades = 0
bebe = crianca = preAdolescente = adolescente = jovem = adulto = idoso = 0


for i in range(0,80): 
    idade = int(input('Digite a sua idade: '))
    idades += idade

    if idade <= 2:
        bebe += 1
    elif idade <= 10:
        crianca += 1
    elif idade <= 14:
        preAdolescente += 1
    elif idade <= 18:
        adolescente += 1
    elif idade <= 21:
        jovem += 1
    elif idade <= 60:
        adulto += 1
    else:
        idoso += 1
 
    if idade > idadeMaior:
        idadeMaior = idade
    if idade < idadeMenor:
        idadeMenor = idade

mediaIdade = idades / 80

print(f'Media das idades: {mediaIdade} anos')
print(f'Idade da pessoa mais velha: {idadeMaior}')
print(f'Idade da pessoa mais nova: {idadeMenor}')
print(f'Numero de bebes: {bebe}')
print(f'Numero de criancas: {crianca}')
print(f'Numero de pre-adolescentes: {preAdolescente}')
print(f'Numero de adolescentes: {adolescente}')
print(f'Numero de jovens: {jovem}')
print(f'Numero de adultos: {adulto}')
print(f'Numero de idosos: {idoso}')


