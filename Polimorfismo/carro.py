from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, status=False):
        super().__init__(marca, modelo)
        self.cor = cor
        self.status = status

    def __str__(self):
        return f'{super().__str__()} | Cor: {self.cor} | Status: {"Ligado" if self.status else "Desligado"}'
        
    def ligar(self):
        self.status = True
        return f'O carro {self.modelo} está ligado!'