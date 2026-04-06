  
def pedir_valor():
    valor_str = input("Qual o valor da conta? ")
    gorjeta_str = input("Qual a porcentagem para a gorjeta? ")

    if not valor_str:
        print("Erro! Nenhum valor foi escrito.")
        return

    if not gorjeta_str:
        print("Erro! Nenhuma porcentagem foi escrita.")
        return

    valor = float(valor_str)
    gorjeta = float(gorjeta_str)

    porcentagem_gorjeta = (gorjeta / 100) * valor

    valor_gorjeta = porcentagem_gorjeta 
    total_conta = valor + valor_gorjeta

    print(f"Total da gorjeta: {valor_gorjeta}")
    print(f"Total com gorjeta: {total_conta}")

pedir_valor()
