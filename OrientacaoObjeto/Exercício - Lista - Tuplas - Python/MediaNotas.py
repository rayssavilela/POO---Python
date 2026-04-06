class Media:

    
    def __init__(self):
        self.notas = []

    def __str__(self):
        return f"{self.notas}"
    

    def notas_alunos(self):
        while True:
            entrada = input("Digite as notas dos alunos separadas por vírgula (OU 'sair' para encerrar): ")
            if entrada == 'sair':
                break
            try:
                notas = [float(n.strip()) for n in entrada.split(",")]
                self.notas.extend(notas)
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
    
    def calcular_media(self):
        if not self.notas:
            print("Nenhuma nota informada.")
            return
        media = sum(self.notas) / len(self.notas)
        print(f"Média final da turma: {media:.2f}")



media = Media()
media.notas_alunos()
media.calcular_media()