tarefas = []

def adicionar_tarefa():
    tarefa = input("\nDigite a nova tarefa: ")

    if tarefa:
        tarefas.append(tarefa)
        print("\nTarefa adicionada com sucesso!\n")
    else:
        print("\nTarefa não pode ser vazia.\n")

def listar_tarefas():
    if tarefas:
        print("\nLista de tarefas:\n")
        indice = 1
        for tarefa in tarefas:
            print(f"{indice}. {tarefa}")
            indice += 1

    else:
        print("\nNenhuma tarefa cadastrada.\n")

def remover_tarefa():
    nome = input("\nDigite o nome exato da tarefa que deseja remover: ")

    if nome in tarefas:
        tarefas.remove(nome)
        print("\nTarefa removida com sucesso!\n")
    else:
        print("\nTarefa não encontrada.\n")
    

def main():
    while True:
        print("\nMenu de Tarefas\n")
        print("1. Adicionar uma nova tarefa")
        print("2. Listar todas as tarefa")
        print("3. Remover uma tarefa pelo nome")
        print("4. Sair")

        opcao = input("\nEscolha uma opção (1-4): ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("\nEncerrando o programa. Até mais!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")



if __name__ == "__main__":
    main()