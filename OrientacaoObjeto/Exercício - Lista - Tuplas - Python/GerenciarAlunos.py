class Aluno:
    def __init__(self, nome: str, idade: int, nota: float):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def exibir(self):
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nota: {self.nota}\n")


class GerenciadorAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_alunos(self):
        dados = input(
            "Digite os dados no formato Nome, Idade, Nota separados por vírgula: "
        ).split(", ")


        if len(dados) % 3 != 0:
            print("Entrada inválida! Use múltiplos de 3 valores.")
            return

        for i in range(0, len(dados), 3):
            try:
                nome = dados[i]
                idade = int(dados[i + 1])
                nota = float(dados[i + 2])

                aluno = Aluno(nome, idade, nota)
                self.alunos.append(aluno)

            except ValueError:
                print(f"Erro ao converter dados: {dados[i:i+3]}")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return

        for aluno in self.alunos:
            aluno.exibir()


gerenciador = GerenciadorAlunos()
gerenciador.adicionar_alunos()
gerenciador.listar_alunos()