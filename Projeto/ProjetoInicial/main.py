from contador import contador_de_frases

frase = input("Digite uma frase: ").strip()

if not frase:
    print("Erro! Nenhuma mensagem foi escrita.")
else:
    resultado = contador_de_frases(frase)
    if resultado:
        print("Contagem de Palavras:")
        for palavra, quantidade in resultado.items():
            print(f"{palavra} : {quantidade}")
    else:
        print("Nenhuma palavra válida foi encontrada")
