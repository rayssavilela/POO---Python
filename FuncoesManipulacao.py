type(10) #Retorna o tipo de um Objeto

isinstance(10.5, int) #Verifica se o Objeto (10.5) pertence a um tipo ou uma tupla de tipos
#Retorna TRUE se for do tipo indicado, e FALSE se não for

len("python") #Retorna o Tamanho de uma String, lista ou tupla

list("abc") #Converte para lista ("a", "b", "c")

dict(nome = "Ana") #Cria um dicionário Saida: {"nome": "Ana"}

set([1, 2, 3]) #Cria um conjunto Saida: {1, 2, 3, 4}

abs(-10) #Retorna o valor absoluto de um numero

round(3.14563) #Arredonda um numero

max(3, 5, 1) #Retorna o maior valor entre os fornecidos

min(3, 5, 1) #Retorna o menor valor entre os fornecidos

sum([3, 5, 1]) #Retorna a soma de uma lista de numeros

list(filter(lambda x : x > 2, [1, 2, 3, 4])) #Filtra elementos de um iterável com base em uma condição Saida: [3, 4]

list(map(lambda x : x * 2, [1, 2, 3])) #Aplica Função a cada elemento de um iterável Saida: [2, 4, 6] 
#Map transforma uma variavel para o tipo que voce quiser, exemplo:
lista = ["1", "2", "3", "4"]

lista_int = list(map(int, lista))

print(lista_int)
# [1, 2, 3, 4]


list(zip([1, 2, 3], ["a", "b", "c"])) #Une dois ou mais iteráveis, criando pares de elementos correspondentes Saida: [(1, "a"), (2, "b"), (3, "c")]

sorted([3, 1, 4, 2]) #Retorna uma nova lista ordenada Saida: [1, 2, 3, 4]

list(reversed([1, 2, 3])) #Retorna um iterador com os elementos de um iterável na ordem inversa Saida: [3, 2, 1]

#lambda argumentos: expressao
soma = lambda a, b: a + b
print (soma(3, 5)) #São uteis para operações simples ou quando precisamos de funções curtas dentro de outras funções

def multiplicador(n): #Função externa
    def multiplica(x): #Closure
        return x * n
    return multiplica #Retorna funcao interna
triplo = multiplicador(3)
valor = triplo(5)
print(valor) #Saida: 15