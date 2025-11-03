numero = 0
while numero >= 0:
    numero = int(input("Digite um numero inteiro positivo (valor negativo para encerrar): "))
    if numero <= 0:
        print('ENCERRADO')
        exit()
    
    contagem = 0
    soma = 0
    
    for x in range (1, numero):
        if x % 2 != 0:
            contagem += 1
            soma += x
            
    print(f"Numeros impares entre 1 e {numero}: {contagem}")
    print(f"Soma dos números impares: {soma}")
    
