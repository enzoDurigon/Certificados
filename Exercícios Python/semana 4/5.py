tempo = int(input('Digite o tempo de conclusão: '))
idade = int(input('Digite sua idade: '))
genero = input('Digite seu gênero: ').strip().lower()
tipo = input('Digite o tipo de corrida: 1- Trilha   2- Asfalto   3- Híbrida: ')
recordes = input('Quebrou recordes?: ').strip().lower()
infracoes = input('Digite as infrações: 1- Corte de caminho   2- Recebimento de ajuda externa   3- Nenhuma: ')

pontosTempo = 0
pontosIdade = 0
pontosGenero = 0
pontosRecorde = 0
pontosInfracao = 0


if tempo < 30:
    pontosTempo += 100
elif tempo >= 30 and tempo <= 60:
    pontosTempo += 100 - (tempo - 30) * (30 / 30)
elif tempo >= 60 and tempo <= 90:
    pontosTempo += 70 - (tempo - 60) * (30 / 30)
elif tempo > 90:
    pontosTempo += 40




if idade < 18:                                                          
    pontosIdade += 20
elif idade >= 18 and idade <= 30:
    pontosIdade += 10
elif idade >= 31 and idade <= 45:
    pontosIdade += 15
elif idade >= 46 and idade <= 60:
    pontosIdade += 20
elif idade > 60:
    pontosIdade += 25    




if genero == 'feminino':
    pontosGenero += 5




if recordes == "sim":
    pontosRecorde += 50


pontosTotal = (pontosTempo + pontosIdade + pontosGenero + pontosRecorde + pontosInfracao)

if infracoes == "1":
    pontosInfracao -= 10
elif infracoes == "2":
    pontosTotal = 0
    print('DESQUALIFICADO DA PROVA')
    pontosTotal = 0
    print(f'Pontuação total: {pontosTotal} pontos.')
    exit()
else:
    pontosInfracao = 0



if tipo == "1":
    pontosTotal += pontosTotal * 1.1




print(f'Pontos ganhos do tempo = {pontosTempo} pontos.')
print(f'Pontos ganhos da idade = {pontosIdade} pontos.')
print(f'Pontos ganhos do gênero = {pontosGenero} pontos.')
print(f'Pontos ganhos do recorde = {pontosRecorde} pontos.')
print(f'Pontos perdidos das infrações = {pontosInfracao} pontos.')

print(f'Pontuação total de {pontosTotal} pontos.')