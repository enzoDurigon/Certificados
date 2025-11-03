nome = input('digite o nome do funcionario: ')
horasSemanais = int(input('digite suas horas semanais: '))
dependentes = int(input('digite o numero de dependentes: '))

pagamentoMensal = ((horasSemanais * 25) * 4)
pagamentoDependentes =  (dependentes * 500)
pagamentoTotal = (pagamentoMensal + pagamentoDependentes)
print(f'O funcionario {nome} ganhara {pagamentoTotal}')