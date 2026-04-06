class Evento:
    """Programa que permita ao organizador ordená-los, de forma que a lista final siga a sequência correta."""

    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
    
    @classmethod
    def listar_eventos(cls):
        print("\nLista atual de eventos:")
        for i, evento in enumerate(cls.eventos_registrados):
            print(f"{i} - {evento}")

    @classmethod
    def corrigir_eventos(cls):
        while True:
            try: 
                posicao = int(input("Informe a posição atual do evento que quer mudar (ou -1 para sair):"))
                
                if posicao == -1:
                    break

                if posicao < 0 or posicao > len(cls.eventos_registrados):
                    print("Posição inválida! Tente novamente")
                    continue

                nova_posicao = int(input("Informe a nova posição do evento:"))

                if nova_posicao < 0 or nova_posicao > len(cls.eventos_registrados):
                    print("Posição inválida! Tente novamente")
                    continue

                 # Remove o evento
                evento = cls.eventos_registrados.pop(posicao)

                 # Insere na nova posição
                cls.eventos_registrados.insert(nova_posicao, evento)

                print("\nEvento movido com sucesso!")
            except ValueError:
                print("Entrada inválida! Tente novamente")
                continue

    @classmethod
    def opcao_escolhida(cls):
        while True:
            print("\n=== MENU ===")
            print("1 - Listar Eventos")
            print("2 - Corrigir Eventos")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cls.listar_eventos()
            
            elif opcao == '2':
                cls.corrigir_eventos()
            
            elif opcao == '3':
                print("Encerrando...")
                break
            
            else:
                print("Opção inválida!")

Evento.opcao_escolhida()
