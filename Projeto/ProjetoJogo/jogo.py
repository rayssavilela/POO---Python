import random

def JogoSorte():

    computador = ['pedra', 'papel', 'tesoura']
    selecionado = random.choice(computador) 

    escolha = input("Escolha qual opção irá jogar:\n" 
    "Pedra\n" 
    "Papel\n" 
    "Tesoura\n").lower() 

    if escolha not in computador:
        print("Escolha inválida")
        return
    print(f"Computador escolheu: {selecionado}") 
        

    if escolha == selecionado:
        print("Empate!")

    elif(
        escolha == "pedra" and selecionado == "tesoura"or 
        (escolha == "papel" and selecionado == "pedra") or 
        (escolha == "tesoura" and selecionado == "papel") 
    ): 
        print("Você venceu!") 
    else: 
        print("Você perdeu!") 

JogoSorte()