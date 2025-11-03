gabarito = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']

alunos = 0
maiorNota = 0
totalNotas = 0
menorNota = 0
outroAlunoUsar = 'sim'

while outroAlunoUsar == 'sim':
    alunos += 1
    acerto = 0

    for resp in range(0, 10):
        resposta = input(f'Digite sua resposta da questao {resp + 1}: ').strip().lower()
        if resposta == gabarito[resp]:
            acerto += 1 
    totalNotas += acerto
    if acerto > maiorNota:
        maiorNota = acerto
    if acerto < menorNota:
        menorNota = acerto
    
    outroAlunoUsar = str(input('Digitar a nota de outro aluno? [SIM OU NAO]: ')).strip().lower()
    
    
media = totalNotas / alunos
print(f"Total de alunos: {alunos}")
print(f"Média das notas: {media:.2f}")
print(f"Maior nota: {maiorNota}")
print(f"Menor nota: {menorNota}")




