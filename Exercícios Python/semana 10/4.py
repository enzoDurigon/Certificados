agenda = {}


def incluirNovoTel(nome, *telefones):
    agenda[nome] = list(telefones)


def incluirTelefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        incluirNovoTel(nome, telefone)


def excluirTelefone(nome, telefone):
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
            

def excluirNome(nome):
    if nome in agenda:
        del agenda[nome]
    else:
        print(f"{nome} não está na agenda.")




incluirNovoTel("Ana", "1234-5678")
incluirNovoTel("João", "5555-5555")
incluirTelefone("Ana", "1111-2222")
incluirTelefone("Maria", "3333-4444")
excluirTelefone("Ana", "1234-5678")
excluirNome("João")


print(agenda)
