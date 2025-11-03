import customtkinter as ctk
import banco

#login: 123 
#senha: 123

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if banco.verificar_login(usuario, senha):
        resultado_login.configure(text="Login feito com sucesso!", text_color="green")
    else:
        resultado_login.configure(text="Usuário ou senha incorretos!", text_color="red")

def exibir_senha():
    if mostrar_senha.get() == 1:
        campo_senha.configure(show="")  
    else:
        campo_senha.configure(show="*")  


#configurando janela 
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry('600x600')


#login

label_usuario = ctk.CTkLabel(app,text="Usuario")
label_usuario.pack(pady=(30, 2))

campo_usuario = ctk.CTkEntry(app,placeholder_text="Digite seu usuario")
campo_usuario.pack(pady=(0 ,20))


label_senha = ctk.CTkLabel(app,text="Senha")
label_senha.pack(pady=(10, 2))

campo_senha = ctk.CTkEntry(app,placeholder_text="Digite sua senha",show="*")
campo_senha.pack(pady=(0, 10))


mostrar_senha = ctk.IntVar(value=0)
check_mostrar_senha = ctk.CTkCheckBox(app, text="Exibir senha", variable=mostrar_senha, command=exibir_senha)
check_mostrar_senha.pack(pady=(0, 20))


botao_login = ctk.CTkButton(app,text="Login",command=validar_login)
botao_login.pack(pady=(10, 10))

resultado_login = ctk.CTkLabel(app,text="")
resultado_login.pack(pady=10)



#rodar aplicativo
app.mainloop()