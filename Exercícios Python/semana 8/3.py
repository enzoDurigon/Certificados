tech = int(input('Digite a quantidade de alunos da germinare tech: '))
business = int(input('Digite a quantidade de alunos da germinare business: '))


crescimentoTech = 0.5
crescimentoBusiness = 0.1

for anos in range(1000):
    business *= (1 + crescimentoBusiness)
    tech *= (1 + crescimentoTech)
    if tech > business:
        print(f'O Germinare Tech ultrapassara o germinare business em {anos} anos')
        break
