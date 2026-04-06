class Pedido:

    pedidos_feitos = ['Sanduiche', 'Refrigerante Zero', 'Suco', 'Sobremesa']

    @classmethod
    def listar_pedidos(cls):
        print(f"\nLista de Pedidos Feitos:")
        for i, ped in enumerate(cls.pedidos_feitos):
            print(f"{i} - {ped}")

    @classmethod
    def remover_ultimo_item(cls):
        if cls.pedidos_feitos:
            print(f"Removendo o ultimo item da lista sendo ele: {cls.pedidos_feitos[-1]}")
            cls.pedidos_feitos.pop()
        else:
            print("A lista está vazia!")

    @classmethod
    def opcao_escolhida(cls):
        while True:
            print("\n=== MENU ===")
            print("1 - Listar Pedido Feito")
            print("2 - Corrigir Pedido Incorreto")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cls.listar_pedidos()
            
            elif opcao == '2':
                cls.remover_ultimo_item()
            
            elif opcao == '3':
                print("Encerrando...")
                break
            
            else:
                print("Opção inválida!")

Pedido.opcao_escolhida()           

