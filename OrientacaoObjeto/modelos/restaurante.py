class Restaurante:
    nome = ''  
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
nome_do_restaurante = restaurante_praca.nome
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

categoria = Restaurante.categoria
restaurante_praca.nome = 'Bistrô'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

restaurante_pizza.ativo = True



restaurantes = [restaurante_pizza, restaurante_praca]

print(dir(restaurante_praca)) #Responsável por mostrar tudo a respeito de uma classe, atributos, métodos e propriedades de um Objeto
print("\n")
print(vars(restaurante_praca)) #Responsável por mostrar um dicionário dos atributos e métodos de uma classe

