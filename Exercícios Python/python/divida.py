valor = int(input('Digite o valor do emprestimo: '))
porcentual = int(input('Digite o valor porcentual (em %): '))
tempo = int(input('Digite o tempo em meses: '))

def calcular_divida(valor, porcentual):
    valor_final_divida = (valor / 100 * porcentual) + valor
    return valor_final_divida

valor_final = calcular_divida(valor, porcentual)

def calcular_parcela(valor_final_divida, tempo):
    parcela_mensal = valor_final_divida / tempo
    return parcela_mensal

print(f'''RESUMO DO EMPRESTIMO
Valor solicitado: R${valor}
Taxa acrescimo: {porcentual}%
Tempo (em meses): {tempo}
Divida Total: R${calcular_divida(valor, porcentual)}
Parcelas Mensais: R${calcular_parcela(valor_final, tempo)}      
''')
