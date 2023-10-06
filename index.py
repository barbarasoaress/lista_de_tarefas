# Inicializando a lista de tarefas vazia
lista_de_tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    lista_de_tarefas.append({"tarefa": tarefa, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(lista_de_tarefas, 1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{i}. {status} {tarefa['tarefa']}")

def marcar_como_concluida():
    listar_tarefas()
    numero_tarefa = int(input("Digite o número da tarefa concluída: ")) - 1
    if 0 <= numero_tarefa < len(lista_de_tarefas):
        lista_de_tarefas[numero_tarefa]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

def excluir_tarefa():
    listar_tarefas()
    numero_tarefa = int(input("Digite o número da tarefa a ser excluída: ")) - 1
    if 0 <= numero_tarefa < len(lista_de_tarefas):
        del lista_de_tarefas[numero_tarefa]
        print("Tarefa excluída com sucesso!")
    else:
        print("Número de tarefa inválido.")

if __name__ == "__main__":
    while True:
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Excluir Tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4/5): ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_como_concluida()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")
