class Convidados:
    """Programa que mostra a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada"""
    lista_convidados = ['Paula', 'Ana', 'Matheus', 'Vitoria']

    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return f'{self.lista_convidados}'
    
    @classmethod
    def listar_convidados(cls):
        print("\nLista atual de convidados:")
        for i, pessoa in enumerate(cls.lista_convidados):
            print(f"{i} - {pessoa}")

    @classmethod
    def adicionar_convidados(cls):
        while True:
            convidado = input("Digite o nome do novo convidado (ou 'sair'): ")
            if convidado.lower() == 'sair':
                break
            if not convidado:
                print("Nome inválido!")
                continue
            try:
                posicao = int(input("Digite a posição que quer incluir este convidado: "))
                if posicao < 0 or posicao > len(Convidados.lista_convidados):
                    print("Posição inválida! Será adicionado ao final.")
                    cls.lista_convidados.append(convidado)
                else:
                    cls.lista_convidados.insert(posicao, convidado)
            except ValueError:
                print("Entrada inválida! Tente novamente")
                continue

    @classmethod
    def opcao_escolhida(cls):
        while True:
            print("\n=== MENU ===")
            print("1 - Listar convidados")
            print("2 - Adicionar convidado")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cls.listar_convidados()
            
            elif opcao == '2':
                cls.adicionar_convidados()
            
            elif opcao == '3':
                print("Encerrando...")
                break
            
            else:
                print("Opção inválida!")

Convidados.opcao_escolhida()
        
    