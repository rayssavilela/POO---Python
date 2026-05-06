from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self):
        return self._nome
    
    #Polimorfismo
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)

"""Este código define uma classe chamada Sobremesa que herda da classe ItemCardapio. A classe Sobremesa possui os seguintes atributos:

nome: herdado de ItemCardapio.
preco: herdado de ItemCardapio.
descricao: específico da classe Sobremesa.
tipo: específico da classe Sobremesa.
tamanho: específico da classe Sobremesa.
O método __str__ é sobrescrito para retornar o nome da sobremesa. Além disso, a classe implementa o método aplicar_desconto, que reduz o preço da sobremesa em 15%.

Lembrando: O método adicionar_no_cardapio presente na classe Restaurante 
é suficiente para adicionar qualquer item do cardápio, incluindo sobremesas ��). Isso ocorre porque a classe Sobremesa 
herda de ItemCardapio, portanto, um objeto da classe Sobremesa também é uma instância de ItemCardapio."""