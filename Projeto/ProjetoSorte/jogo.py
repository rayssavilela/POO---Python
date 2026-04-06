import random

def sorte():
    
    sorteado = random.randint(1, 100)
    tentativas = 0
    while True:
        try:
            escolha = int(input("Defina um numero de 1 até 100: "))
            if not 1 <= escolha <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")
            tentativas += 1

            if escolha == sorteado:
                print(f"Parabéns! Você acertou o número {sorteado}.")
                break
            elif escolha < sorteado:
                print(f"Muito baixo! Tente novamente: {escolha}.")
            elif escolha > sorteado:
                print(f"Muito alto! Tente novamente: {escolha}")

        except ValueError as e:
            print(f"Entrada inválida: {e}")


sorte()