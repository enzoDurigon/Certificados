lucas = wellington = gabriella = branco = votos = votosValidos = 0
continuar = 'sim'

while continuar == 'sim':
    print('''    ESCOLHA O SEU CANDIDATO:
    [1] LUCAS
    [2] WELLINGTON
    [3] GABRIELLA   
    [4] VOTO EM BRANCO''')
    escolha = int(input('Digite o numero do seu candidato: '))
    
    if escolha == 1:
        lucas += 1
        votosValidos += 1
    elif escolha == 2:
        wellington += 1
        votosValidos += 1
    elif escolha == 3:
        gabriella += 1
        votosValidos += 1
    elif escolha == 4:
        branco += 1
    votos += 1

    
    continuar = input('Quer continuar? [SIM OU NAO]: ').lower()

if votosValidos > 0:
    porcemLucas = (lucas / votosValidos) * 100
    porcemWellington = (wellington / votosValidos) * 100
    porcemGabriella = (gabriella / votosValidos) * 100
    porcemBranco = (branco / votos) * 100  

    if lucas > wellington and lucas > gabriella:
        vencedor = "LUCAS"
        porcem = porcemLucas
    elif wellington > lucas and wellington > gabriella:
        vencedor = "WELLINGTON"
        porcem = porcemWellington
    elif gabriella > lucas and gabriella > wellington:
        vencedor = "GABRIELLA"
        porcem = porcemGabriella
    else:
        vencedor = "EMPATE"
        print('Empate, sera decidido no segundo turno. ')
        exit()

print(f'o vencedor foi: {vencedor}')
print(f'Porcentagem de votos do vencedor: {porcem:.2f} %')
