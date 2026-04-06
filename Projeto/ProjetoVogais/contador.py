
def limpar_texto(texto):
    texto = texto.lower()#transforma o texto em letra minúscula
    caracteres = ",.!?|/:;'(){}[]"
    for char in caracteres: #para cada caractere dentro da lista
        texto = texto.replace(char, "")#Eu irei trocar os caracteres por um valor vazio
    return texto


def validar_vogais(frase):
    frase = limpar_texto(frase)

    if not frase.strip(): #se nada escrito
        return 0

    vogais = "aeiou"
    contador = 0

    for letra in frase:
        if letra in vogais:
            contador += 1

    return contador



frase = input("Digite uma frase: ").strip()

if not frase:
    print("Erro! Nenhuma mensagem foi escrita.")
else:
    total_vogais = validar_vogais(frase)
    print(f"O texto contém {total_vogais} vogais.")


    