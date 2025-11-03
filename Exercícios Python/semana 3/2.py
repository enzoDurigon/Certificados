renda = float(input('Qual sua renda mensal atual? '))
emprestimo = float(input('Quanto deseja pegar de emprestimo? '))
score = str(input("Seu Score de crédito é acima de 450 pontos? "))
dividas = str(input("Você possui dívidas ativas? "))
funcionario = str(input("Você é funcionário público? "))
compartilhar = str(input("Você concorda em compartilhar seus dados de outros bancos através do open banking? "))
respostasSim = 0 
dobroDaRenda = (emprestimo * 2) <= renda

if score == "sim":
    respostasSim +=1

if dividas == "nao":
    respostasSim +=1

if funcionario == "sim":
    respostasSim +=1

if compartilhar == "sim":
    respostasSim +=1

if dobroDaRenda is True:
    respostasSim +=1
    


if respostasSim == 5:
    classificacao = "Aprovação total"
    valor_aprovado = emprestimo
elif respostasSim == 3 or respostasSim == 4:
    classificacao = "Aprovado com desconto"
    valor_aprovado = (emprestimo / 100) * 60
elif respostasSim == 2:
    classificacao = "Aprovado com restrições"
    valor_aprovado = (emprestimo / 100) * 20
else:
    classificacao = "Não aprovado"
    valor_aprovado = 0
if dobroDaRenda is False:
    classificacao = "Não aprovado"
    valor_aprovado = 0

print(f"Classificação: {classificacao}")
print(f"Valor aprovado: R${valor_aprovado:.2f}")