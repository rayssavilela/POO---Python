print('A','L','U','R','A',sep='\n')

# Criação das Variáveis
nome = 'Lais'
idade = 24

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))



lista = [1,’olá mundo’,True,9.7]
tupla = (1,’olá mundo’,True,9.7)
         
# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)


# Definindo uma tupla de coordenadas geográficas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])


livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Fabrício Silva',
    'ISBN': '12345',
    'preco': 59.90,
    'em_estoque': True
}

#para atualizar um valor em uma lista em dicionários:

livro['preco'] = 69.90

livro.update({'preco': 69.90})

# esses dois metodos você consegue acessar o fator "preço" em uma lista

credenciais_clientes = {
    'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
    'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
    'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
}

#Para enviar um alerta ao usuario bob que esta inactivo, usando os dicionarios:

alerta = 'Enviar alerta!' if credenciais_clientes['bob456']['status'] == 'inactive' else 'Sem alerta'

#Para criar um dicionário com informações de uma pessoa, você pode utilizar a seguinte solução:
pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}

#Para fazer a atualização de um valor, adicionar um item e remover uma informação, você pode usar o seguinte raciocínio:

# Atualização de Idade
pessoa['idade'] = 31

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']

#Uma possível abordagem para criar um dicionário que apresente os números de 1 a 5 e seus respectivos quadrados é a seguinte:
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

#Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

#Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)