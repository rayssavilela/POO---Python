def validando_cpf():
    cpf = input("Digite o CPF do cliente: ")

    if not cpf.isdigit(): #isdigit() é um método de string em Python que verifica se todos os caracteres da string são números. Se sim, retorna TRUE
        print("Erro: O CPF deve conter apenas números.")
        return

    if len(cpf) != 11:
        print("Erro: O CPF deve ter exatamente 11 dígitos.")
        return

    print("CPF válido!")
    

validando_cpf()
