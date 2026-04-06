class Campanha:

    voluntarios = []
    def __init__(self, nome):
        self._nome = nome
        

    def __str__(self):
        return f"{self._nome}"
    
    @classmethod
    def inscricao_voluntarios(cls):
        while True:
            nome = input(f"Digite o nome do voluntário (ou 'sair' para encerrar):")
            if nome.lower() == "sair": 
                break   
            voluntario = Campanha(nome)
            cls.voluntarios.append(voluntario)
        
        print("\nLista de Voluntários: ")
        for candidato in cls.voluntarios:
            print(candidato)

Campanha.inscricao_voluntarios()