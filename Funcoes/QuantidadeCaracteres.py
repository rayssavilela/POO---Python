def quantidade_caracteres(palavra):
    return palavra

palavra = input("Digite uma palavra: ")

if len(palavra) > 10:
    print("Excedeu o limite de caracteres")

else:
    print(f"Essa palavra tem {len(palavra)} caracteres.")