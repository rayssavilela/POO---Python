def limpar_texto(texto):
    texto = texto.lower() #transforma o texto em letra minúscula
    caracteres = " , . ! ? | / : ; ' () {} [] "
    for char in caracteres: #para cada caractere dentro da lista
        texto = texto.replace(char, "") #Eu irei trocar os caracteres por um valor vazio
    return texto

def contador_de_frases(frase):
    frase = limpar_texto(frase)

    if not frase.strip(): 
        return {}
    
    palavras = frase.split() #divide as palavras da frase
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
  
    return contagem