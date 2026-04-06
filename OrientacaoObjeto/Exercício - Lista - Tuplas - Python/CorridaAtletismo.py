class Corrida:
    participantes = ['Ana', 'Carlos', 'Pedro', 'Vitor', 'Paula']

    @classmethod
    def listar_participantes(cls):
        print("\nLista atual de participantes:")
        for i, participante in enumerate(cls.participantes):
            print(f"{i} - {participante}")

    
    @classmethod
    def corrigir_corrida(cls):
        while True:
            try:
                posicao = int(input("Digite a posição do Participante que deseja retirar da lista (-1 para encerrar): ")) 
                if posicao == -1:
                    break
                if posicao < 0 or posicao > len(cls.participantes):
                        print("Posição inválida! Tente novamente")
                        continue
                else: 
                    participante_antigo = cls.participantes.pop(posicao)
                    print(f"Participante {participante_antigo} removido com sucesso")

                participante = input("Digite o nome do participante correto (ou 'sair' para encerrar):")
                if participante.lower() == 'sair':
                    cls.participantes.insert(posicao, participante_antigo)
                    break
                if not participante.strip():
                    print("Nome inválido! Será colocado de volta o participante antigo.")
                    cls.participantes.insert(posicao, participante_antigo)
                    continue

                cls.participantes.insert(posicao, participante)
                print(f"Participante '{participante}' inserido com sucesso!\n")
            except ValueError:
                print("Entrada inválida! Tente novamente")
                continue

    @classmethod
    def opcao_escolhida(cls):
        while True:
            print("\n=== MENU ===")
            print("1 - Listar Participantes")
            print("2 - Corrigir Corrida")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cls.listar_participantes()
            
            elif opcao == '2':
                cls.corrigir_corrida()
            
            elif opcao == '3':
                print("Encerrando...")
                break
            
            else:
                print("Opção inválida!")

Corrida.opcao_escolhida()           
