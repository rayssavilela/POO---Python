from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()   #Faz com que toda primeira letra fica maiúscula
        self._categoria = categoria.upper() #Faz com que todas as letras ficam maiúsculas
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod #É um método criado que se instância a própria classe, por exemplo, ele somente vai formatar em lista todos os atributos da CLASSE
    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌' #Um atributo com '_' é um atributo privado, ou seja, não se deve editá-lo

    def alternar_estado(self): #Método criado para os OBJETOS alterando os atributos
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media