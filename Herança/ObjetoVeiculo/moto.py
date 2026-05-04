# 5- Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. 
# Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.


from veiculo import Veiculo

class Moto(Veiculo):
    
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

# 6- Implemente o Método Especial __str__ na Classe Filha (Moto): Adicione um método especial __str__ à classe Moto que estenda o método da classe pai (Veiculo).
    def __str__(self):
        return f'{super().__str__()} | Tipo: {self.tipo}'