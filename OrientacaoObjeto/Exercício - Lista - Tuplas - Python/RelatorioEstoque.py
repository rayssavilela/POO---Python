class Estoque:
    """Programa que le as informações dos estoques e gera um relatório com todos os produtos juntos"""
    def __init__(self):
        self.estoque1 = ()
        self.estoque2 = ()
    
    def __str__(self):
        return f"Estoque combinado: {self.unificar()}"
    

    def adicionar_estoque1(self):
        while True:
            entrada = input("Produtos do estoque 1 (separados por vírgula): \nDigite 'sair' para encerrar: ")
            if entrada.lower() == 'sair':
                break
            itens = tuple(item.strip() for item in entrada.split(",")) #Split separa os itens por virgura + Strip tira espaço vazio 
            self.estoque1 += itens


    def adicionar_estoque2(self):
        while True:
            entrada = input("Produtos do estoque 2 (separados por vírgula): \nDigite 'sair' para encerrar: ")
            if entrada.lower() == 'sair':
                break
            itens = tuple(item.strip() for item in entrada.split(",")) #Split separa os itens por virgura + Strip tira espaço vazio 
            self.estoque2 += itens

    def unificar(self):
        estoque_unificado = self.estoque1 + self.estoque2
        print(f"Estoque combinado:\n{estoque_unificado}")

estoque = Estoque()

estoque.adicionar_estoque1()
estoque.adicionar_estoque2()

estoque.unificar()