salarioInicial = float(input('Digite o salario inicial: '))
anoContratacao = int(input('Digite o ano da sua contratacao: '))
anoSistema = 2024
anoNaEmpresa = anoSistema - anoContratacao
salario1ano = 0 
if salarioInicial < 1000:
    print('O salario minimo e R$ 1000.00.')
    exit()

if anoContratacao < 1995 or anoContratacao > anoSistema:
    print('A data precisa estar entre 1995 a 2024.')
    exit()

salarioNovo = salarioInicial
aumentoPorcentagem = 1.5
if anoNaEmpresa <= 1:
    for ano in range(anoContratacao, anoSistema):
        salarioNovo += salarioNovo * (aumentoPorcentagem / 100)
        aumentoPorcentagem *= 1.1
    
    aumentoTotalporcentagem = ((salarioNovo - salarioInicial) / salarioInicial) * 100

    
else:
    for ano in range(anoContratacao, anoSistema):
        salario1ano += salarioInicial * (aumentoPorcentagem / 100) + salarioInicial
        salarioNovo += ((salarioNovo / 100) * 10) * (anoNaEmpresa - 1) + (salarioInicial * 0.015)
    
    aumentoTotalporcentagem = ((salarioNovo - salarioInicial) / salarioInicial) * 100
    
print(f"Salário inicial: R$ {salarioInicial:.2f}")
print(f"Salário novo: R$ {salarioNovo:.2f}")
print(f"Percentual de aumento: {aumentoTotalporcentagem:.2f}%")