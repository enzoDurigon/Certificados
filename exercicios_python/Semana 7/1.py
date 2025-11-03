nome = str(input('Digite seu nome: '))
email = input('Digite seu email: ')

def validar_email_usuario(email):
    arroba = '@' in email
    com = '.com.br' in email
    return arroba and com

if validar_email_usuario(email):
    print('Email valido.')
else: 
    print('Email invalido.')


