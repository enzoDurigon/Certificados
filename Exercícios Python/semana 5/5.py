divida = float(input('Digite o valor da divida: '))
pagamentoMes = float(input('Digite o valor do pagamento mensal: '))
mes = 1

while divida > 0:
    print(f'MES {mes} ------ R$ {divida:.2f}')
    
    if pagamentoMes >= divida:
        pagamento = divida  
    else:
        pagamento = pagamentoMes  
    
    divida -= pagamento  
    
    mes += 1

print('FIM DA DIVIDA')
