class Livro:

    livros = [] # lista para armazenar todos os livros
    def __init__(self, titulo, autor, ano_publicacao, disponivel = True):
        self._titulo = titulo
        self._autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel
        Livro.livros.append(self)  # adiciona o livro à lista

    def __str__(self):
        self.disponivel = "Livro Disponível ✅" if self.disponivel else "Livro já está emprestado ❌"
        return f"""O livro de nome {self._titulo} publicado no ano de {self.ano_publicacao} 
        e escrito pelo autor {self._autor} se encontra com a disponibilidade: {self.disponivel}"""
    
    def emprestar(self):       
        self.disponivel = not self.disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        return [livro for livro in Livro.livros 
                if livro.ano_publicacao == ano and livro.disponivel]


    

