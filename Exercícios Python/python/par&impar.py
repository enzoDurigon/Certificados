numero = par = impar = soma = 0


for numeros in range(0, 10):
    numero = int(input('Digite um Numero: '))
    soma += numero

    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

  
print(f'A soma dos numero digitados é {soma}.')
print(f'{par} numeros sao pares.')
print(f'{impar} numeros sao impares.')