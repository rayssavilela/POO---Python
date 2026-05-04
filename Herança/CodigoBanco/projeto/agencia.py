from CodigoBanco.projeto.banco import Conta_Banco

class Agencia(Conta_Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero
