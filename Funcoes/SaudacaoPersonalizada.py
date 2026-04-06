def saudacao_personalizada(hora):

    if hora < 12:
        return "Bom dia!"

    elif hora >= 12 and hora <= 18:
        return "Boa Tarde!"

    else:
        return "Boa Noite!"

hora = int(input("Digite a hora atual (0 - 23h): "))
print(saudacao_personalizada(hora))