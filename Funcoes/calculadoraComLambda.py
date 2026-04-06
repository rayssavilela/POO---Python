#Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, 
#multiplicar e dividir dois números.

#Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) 
#e exiba o resultado correspondente.

def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))   
    op = input("Digite a operação (| + | - | * | / |): ")

    match op: 
        case "+":
            soma = lambda num1, num2: num1 + num2
            print(f"O resultado é: {soma(num1, num2)}")
        case "-":
            subtrai = lambda num1, num2: num1 - num2
            print(f"O resultado é: {subtrai(num1, num2)}")
        case "/":
            dividir = lambda num1, num2: num1 / num2
            print(f"O resultado é: {dividir(num1, num2)}")
        case "*":
            multiplicar = lambda num1, num2: num1 * num2
            print(f"O resultado é: {multiplicar(num1, num2)}")
        case _:
            print("Opção inválida")

calculadora()

#Outra forma de resolver:

soma = lambda x, y: x + y 

subtrai = lambda x, y: x - y 

multiplica = lambda x, y: x * y 

divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero" 

x = float(input("Digite o primeiro número: ")) 

y = float(input("Digite o segundo número: ")) 

operacao = input("Escolha a operação (| + | - | * | / |): ") 
 
if operacao == '+': 
    print(f"O resultado é: {soma(x, y)}") 
elif operacao == '-': 
    print(f"O resultado é: {subtrai(x, y)}") 
elif operacao == '*': 
    print(f"O resultado é: {multiplica(x, y)}") 
elif operacao == '/': 
    print(f"O resultado é: {divide(x, y)}") 
else: 
    print("Operação inválida") 


#Forma mais pratica:


operacoes = { 

    '+': soma,  

   '-': subtrai, 

    '*': multiplica, 

    '/': divide 

} 

if operacao in operacoes:  

   resultado = operacoes[operacao](x, y)  

   print(f"O resultado é: {resultado}")  

else:  

   print("Operação inválida") 