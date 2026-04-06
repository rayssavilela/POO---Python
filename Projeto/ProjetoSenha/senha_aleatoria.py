import random
 
def gerar_senha():
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiais = "!@#$%&*"
 
    senha = [
        random.choice(maiusculas), #Utilizar random.choice() para selecionar uma letra maiúscula, uma letra minúscula, um número e um caractere especial.
        random.choice(minusculas),
        random.choice(numeros),     
        random.choice(especiais)    
    ]
 
    todos_caracteres = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8)) #extend, Armazenar esses caracteres iniciais em uma lista chamada senha, k=8 → quantidade de elementos sorteados
    random.shuffle(senha) #Utilizar random.shuffle(senha) para reorganizar os caracteres da lista, 
    #para evitar que os primeiros caracteres sejam sempre das categorias fixas, garantindo mais aleatoriedade na senha final.
    return ''.join(senha) #Converter a lista senha em uma string utilizando ''.join(senha).
 
print(f"Senha gerada: {gerar_senha()}")