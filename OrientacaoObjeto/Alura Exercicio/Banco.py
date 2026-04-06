# 1) Crie uma classe chamada `ContaBancaria` com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:

    contas = []
    
    def __init__(self, titular, saldo, ativo = False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo
        ContaBancaria.contas.append(self)
# 2) Na classe ContaBancaria, adicione um método especial `__str__` que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f"{self.titular} - {self.saldo}"
    
    @classmethod
    def listarContas(cls):
        print(f"{'Titular'.ljust(25)} - {'Saldo Conta'.ljust(15)} | {'Status'}")
        for conta in cls.contas:
            print(f"{conta.titular.ljust(25)} - {str(conta.saldo).ljust(15)} | {conta.ativo}")

# 3) Adicione um método de classe chamado `ativar_conta` à classe `ContaBancaria` que define o atributo ativo como `True`. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    def ativarconta(self):
        self.ativo = not self.ativo
    

conta1 = ContaBancaria('Rayssa', 10000)
conta2 = ContaBancaria('Tabata', 5000)
conta3 = ContaBancaria('Carmen', 5000)

conta3.ativarconta()

ContaBancaria.listarContas()

# 4) Refatore a classe `ContaBancaria` para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
class ContaBancariaPythonica:
    
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
    def ativar_conta(self):
        self._ativo = True
# 5) Crie uma instância da classe e imprima o valor da propriedade titular.
conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")


# 6) Crie uma classe chamada `ClienteBanco` com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta


cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")