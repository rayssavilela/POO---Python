class Concurso:
    """Programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente."""
    concorrentes = []

    def __init__(self, nome, nota):
        self._nome = nome
        self.nota = nota
        Concurso.concorrentes.append(self)

    def __str__(self):
        return f"{self._nome.ljust(25)} | {self.nota}"
    
    @classmethod
    def listar_concorrentes(self):
        print(f"{'Nome Participante'.ljust(25)} | {'Nota Participante'}")
        for participante in self.concorrentes:
            print(f"{participante._nome.ljust(25)} | {str(participante.nota)}")

    @classmethod
    def ordenar_concorrentes(cls):
        cls.concorrentes.sort(key=lambda participante: participante.nota)

nota1 = Concurso('Ana', 5)
nota2 = Concurso('Luan', 6)
nota3 = Concurso('Paulinia', 3)
nota4 = Concurso('Vitor', 0)
nota5 = Concurso('Wesley', 10)

Concurso.listar_concorrentes()
Concurso.ordenar_concorrentes()
print("\n")
print("Lista Ordenada dos Participantes:\n")
Concurso.listar_concorrentes()
    

