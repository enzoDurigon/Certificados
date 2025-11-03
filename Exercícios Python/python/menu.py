n1 = int(input('Digite o Primeiro Numero: '))
n2 = int(input('Digite o Segundo Numero: '))
opcao = 0


while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NUMERO           
    [4] NOVO NUMERO
    [5] SAIR''')
    opcao = int(input('Escolha a sua opcao: '))
      
    if opcao == 1:
        resultado = n1 + n2
        print(f'O resultado da soma é {resultado}')


    elif opcao == 2:
        resultado = n1 * n2
        print(f'O resultado da multiplicacao é {resultado}')

    elif opcao == 3:
        if n1 > n2:
            resultado = n1
        else:
            resultado = n2
        print(f'O maior numero é {resultado}')

    if opcao == 4:
        print('Informe os numero novamente.')
        n1 = int(input('Digite o Primeiro Numero: '))
        n2 = int(input('Digite o Segundo Numero: '))
    
    if opcao == 5:
        print('-=-=-=-=-=-=-=-=-=-=-=-=')
print('FIM')
exit()