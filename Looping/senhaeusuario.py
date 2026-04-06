
while True:

    usuario = input("Digite seu Nome de Usuário: ")
    senha = input("Digite sua senha: ")

    if len(usuario) < 5:
        print("O nome de Usuário deve ter ao menos 5 caracteres")
        continue

    if len(senha) < 8:
        print("A senha deve ter ao menos 8 caracteres")
        continue #Se a condição nao for atingida, ele ira mostrar o print e ira retornar o codigo do inicio, ignorando o resto do codigo, do print de cadastro efetuado com sucesso.

    print("Cadastro Efetuado com Sucesso!")
    break