tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Índice inválido!")

def listar_tarefas():
    if tarefas:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")
    else:
        print("\nA lista de tarefas está vazia.")

while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a nova tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == '2':
        if tarefas:
            indice = int(input("Digite o índice da tarefa a ser removida: ")) - 1
            remover_tarefa(indice)
        else:
            print("Não há tarefas para remover.")
    elif opcao == '3':
        listar_tarefas()
    elif opcao == '4':
        print("Obrigado por usar o gerenciador de tarefas!")
        break
    else:
        print("Opção inválida. Tente novamente.")
