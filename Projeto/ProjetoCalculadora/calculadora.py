def somar(num1, num2):
    return num1 + num2
 
def subtrair(num1, num2):
    return num1 - num2
 
def multiplicar(num1, num2):
    return num1 * num2
 
def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2

def conta():
  
    try:    
        num1 = float(input("Defina o primeiro numero: "))
        num2 = float(input("Defina o segundo numero: "))
        operacao_escolha = input("Defina o tipo de Operação matemática: ")
        operacao = ['+', '-', '*', '/']
        if operacao_escolha not in operacao:
            print("Operação inválida, tente novamente somente operações validas")
            return
        if operacao_escolha == "+":
            resultado = somar(num1, num2)
        elif operacao_escolha == "-":
            resultado = subtrair(num1, num2)
        elif operacao_escolha == "*":
            resultado = multiplicar(num1, num2)
        elif operacao_escolha == "/":
            resultado = dividir(num1, num2)
 
        print(f"Resultado: {resultado}")
        
            
    except ValueError as e:
        print("Erro: Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
 
conta()

    