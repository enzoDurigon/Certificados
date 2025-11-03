idade1 = int(input('Digite a idade da primeira pessoa: '))
idade2 = int(input('Digite a idade da segunda pessoa: '))

if idade1 <= 17:
    preco = 15
elif idade1 > 18 and idade1 <= 59: 
    preco = 30
elif idade1 > 60:
    preco = 20


if idade2 <= 17:
    preco2 = 15
elif idade2 > 18 and idade2 <= 59: 
    preco2 = 30
elif idade2 > 60:
    preco2 = 20


precoTotal = preco + preco2


print(f'A primeira pessoa ira pagar R$ {preco}.')
print(f'A segunda pessoa ira pagar R$ {preco2}.')
print(f'O total a ser pago pelos dois ingressos sao R$ {precoTotal}.')