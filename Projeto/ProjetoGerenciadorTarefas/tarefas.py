def GerenciarTarefas():
    tarefas = []

    while True:
        escolha = input("Defina o que gostaria de fazer:\n" \
            "1 - Adicionar Tarefa\n" \
            "2 - Visualizar Tarefas\n" \
            "3 - Remover Tarefa\n" \
            "4 - Sair\n" \
            "Escolha uma opção: ")
        
        match escolha: 
                case "1":
                    afazer = input("Infome o afazer que deseja incluir na lista: ").strip()
                    if afazer:  # Verifica se a string não está vazia
                        tarefas.append(afazer)
                        print("Tarefa adicionada!")
                    else:
                        print("Erro: A tarefa não pode estar vazia.")

                case "2":
                    if not tarefas:
                         print("Nenhuma tarefa cadastrada.")
                    else:
                        print("Gerenciador de Tarefas:\n")
                        contador = 0
                        for tarefa in tarefas:
                            print(f"{contador}. {tarefa}\n")
                            contador += 1

                case "3":
                    if not tarefas:
                        print("Erro: Nenhuma tarefa para remover.")
                    else:
                        try:
                                numeroTarefa = int(input("Digite o número da tarefa a ser removida: "))
                                if 0 <= numeroTarefa < len(tarefas):
                                    removida = tarefas.pop(numeroTarefa)
                                    print(f"Tarefa '{removida}' removida!")
                                else:
                                    print("Erro: Índice inválido! Digite um número válido.")
                        except ValueError:
                            print("Erro: Entrada inválida! Digite um número.")
                        
                case "4":
                    print("Saindo da lista de Afazeres!")
                    break
                case _:
                    print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")


GerenciarTarefas()     
            

               