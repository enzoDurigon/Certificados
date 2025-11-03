import sqlite3

conexao = sqlite3.connect("Logins.db")
cursor = conexao.cursor()
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
        )
""")

conexao.commit()




def cadastrar_usuario(usuario, senha):
    try:
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False  
    
cadastro = cadastrar_usuario("123", "123")

def verificar_login(usuario, senha):
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    return cursor.fetchone()

def fechar_banco():
    conexao.close()