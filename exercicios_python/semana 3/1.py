senha = input('Digite sua senha: ')
maiusculo = any(s.isupper() for s in senha)
if maiusculo is False:
    print('Sua senha precisa ter pelo menos um caractere maiusculo.')

minusculo = any(s.islower() for s in senha)
if minusculo is False:
    print('Sua senha precisa ter pelo menos um caractere minusculo.')

especiais = ['!', '@', '#', '$', '%']
especial = any(s in especiais for s in senha)
if especial is False:
    print('Sua senha precisa ter pelo menos um caractere especial.')

comprimento = len(senha) >= 8
if comprimento is False:
    print('Sua senha precisa ter pelo menos 8 caracteres.')

if comprimento and maiusculo and minusculo and especial:
    print('Sua senha atende os critérios necessários e é válida.')