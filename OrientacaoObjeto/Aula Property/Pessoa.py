class Pessoa:

    pessoas = []  # lista da classe

    def __init__(self, nome, idade, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)
  
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'
    
    @classmethod
    def listar_pessoas(cls):
        print(f"{'Nome'.ljust(10)} | {'Idade'.ljust(10)} | {'Profissão'}")
        for pessoa in cls.pessoas: 
            print(f"{pessoa.nome.ljust(10)} | {str(pessoa.idade).ljust(10)} | {pessoa.profissao}")

    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        if self.profissao:
            return f'Parabéns pela sua profissão de {self.profissao}'
        else:
            return f'Olá, sou {self.nome}'
        
pessoa1 = Pessoa('Gabriela', 20, 'Dentista')
pessoa2 = Pessoa('Carlos', 30, 'Engenheiro')
pessoa3 = Pessoa('Jaque', 22)
# Imprimindo informações iniciais
Pessoa.listar_pessoas()
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()
print("Informações após aniversário:")
Pessoa.listar_pessoas()
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao())
print(pessoa2.saudacao())
print(pessoa3.saudacao())
