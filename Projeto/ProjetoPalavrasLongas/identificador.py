
def limpar_texto(texto):
    texto = texto.lower()#transforma o texto em letra minúscula
    caracteres = ",.!?|/:;'(){}[]"
    for char in caracteres: #para cada caractere dentro da lista
        texto = texto.replace(char, "")#Eu irei trocar os caracteres por um valor vazio
    return texto

def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.strip(): #divide a frase em um dicionario
        return 0
    
    palavras = frase.split()
    palavras_longas = []
    for palavra in palavras:
        if len(palavra) >= 10:
            palavras_longas.append(palavra)
        
    if palavras_longas:
        print("Palavras longas encontradas: ")
        for p in palavras_longas:
            print(p)     
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")   

frase = input("Digite uma frase: ").strip()

contar_palavras(frase)