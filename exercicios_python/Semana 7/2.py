from datetime import datetime

nascimento1 = input('Digite a data de nascimento da primeira pessoa. (ano-mes-dia):')
nascimento2 = input('Digite a data de nascimento da segunda pessoa. (ano-mes-dia):')

data1 = datetime.strptime(nascimento1, "%Y-%m-%d") 
data2 = datetime.strptime(nascimento2, "%Y-%m-%d") 



def calcular_diferenca_idade(data1, data2): 
    ano = data1.year - data2.year
    mes = data1.month - data2.month
    dia = data1.day - data2.day
    return ano, mes, dia

ano, mes, dia = calcular_diferenca_idade(data1, data2)

print(f'A diferenca de idade e de {ano} anos, {mes} meses, {dia} dias')