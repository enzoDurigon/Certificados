usuario = input('Digite o seu usuario: ').lower() .split()
senha =  input('Digite o sua senha: ').lower() .split()
    

while usuario == senha:
    print('O SEU USUARIO NAO PODE SER IGUAL A SENHA.')
    usuario = input('Digite o seu usuario: ').lower() .split()
    senha =  input('Digite o sua senha: ').lower() .split()
    
if usuario != senha:
    print('USUARIO E SENHA VALIDA. ')
    exit()

