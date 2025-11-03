import math 


entradaHora = int(input("Digite a hora da entrada: " ))
entradaMinuto = int(input("Digite os minutos da entrada: " ))
saidaHora = int(input("Digite a hora da saida: "))
saidaMinuto = int(input("Digite os minutos da saida: "))

minutosEntrada = entradaHora * 60 + entradaMinuto
minutosSaida = saidaHora * 60 + saidaMinuto

if minutosSaida < minutosEntrada:
    minutosSaida += 24 * 60

duracaoHoras = math.ceil((minutosSaida - minutosEntrada) / 60)

if duracaoHoras <= 2:
    valorTotal = duracaoHoras * 1
elif duracaoHoras <= 3:
    valorTotal = duracaoHoras * 1.40
elif duracaoHoras >= 5:
    valorTotal = duracaoHoras * 2



print(f'Duracao no estacionamento: {duracaoHoras} horas')
print(f"Valor total a pagar: R$ {valorTotal:.2f}")