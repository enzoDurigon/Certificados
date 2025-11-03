alunos = []
quantidadeAlunos = int(input('quantos alunos tem na turma?: '))

for i in range(0, quantidadeAlunos):
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input(f'Digite a nota 1 do aluno {nome}: '))
    nota2 = float(input(f'Digite a nota 2 do aluno {nome}: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])
situacao = 'Aprovado' if media >= 7 else 'Reprovado'


for x, aluno in enumerate(alunos, 1):
    nome, nota1, nota2, media, = aluno
    print(f"{x}. Nome: {nome} | Nota 1: {nota1} | Nota 2: {nota2} | Média: {media:.2f} | Situação: {situacao}")
