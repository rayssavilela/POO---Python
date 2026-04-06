class Despensa:
    """Programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado."""
    itens = []

    def __init__(self, nome, quantidade):
        self._nome = nome
        self.quantidade = quantidade 
        Despensa.itens.append(self)   

    def __str__(self):
        return f"{self._nome.ljust(25)} | {self.quantidade}"
    
    @classmethod
    def listar_inventario(self):
        print(f"{'Itens'.ljust(25)} | {'Quantidade'}")
        for item in self.itens:
            print(f"{item._nome.ljust(25)} | {str(item.quantidade)}")

    @classmethod
    def verificar_lista(self):
        nome = input('Digite o item que você deseja verificar: ')
        encontrado = False
        for item in self.itens:
            if item._nome.lower() == nome.lower():
                encontrado = True
                break         
        if encontrado:
            print(f"O item {nome} está presente no inventário")
        else:
            print(f"O item {nome} precisa ser comprado")

item1 = Despensa('Açucar', 10)
item2 = Despensa('Danone', 2)
item3 = Despensa('Arroz', 4)    
item4 = Despensa('Ração', 1)

Despensa.verificar_lista()
Despensa.listar_inventario()