estoque = {}

def adicionar_livro():
    titulo = input("\nTitulo do livro: ").strip()
    qtd = int(input("\nQuantidade a adicionar: "))

    if titulo in estoque:
        estoque[titulo] += qtd
    else:
        estoque[titulo] = qtd
    print(f"\n{qtd} unidade(s) de '{titulo}' adicionada(s).\n")
     
def remover_livro():
    titulo = input("\nTitulo do livro: ").strip()

    if titulo not in estoque:
        print("\nLivro não encontrado no estoque.\n")
        return
    
    qtd = int(input("\nQuantidade a remover: "))

    if qtd > estoque[titulo]:
        print(f"\nNão há unidades suficientes para remover. Estoque atual: {estoque[titulo]}")
        return
    
    estoque[titulo] -= qtd
    print(f"\n{qtd} unidade(s) removida(s) de '{titulo}'.\n")

    if estoque[titulo] == 0:
        print(f"\nEstoque do livro '{titulo}' zerado.\n")
     
def consultar_livro():
    titulo = input("\nTitulo do livro: ").strip()

    if titulo in estoque:
        print(f"\nQuantidade disponível de '{titulo}': {estoque[titulo]}")
    else:
        print("\nLivro não está no estoque.\n")

def mostrar_estoque():
    if not estoque:
        print("\nEstoque vazio\n")
        return
    
    print("\nLivros em estoque:\n")
    for titulo in sorted(estoque.keys()):
        print(f"{titulo}: {estoque[titulo]}")


def main():
    while True:
        print("\n---MENU---\n")
        print("1. Adicionar livro ao estoque")
        print("2. Remover unidades de um livro")
        print("3. Consultar quantidade de um livro")
        print("4. Mostrar todos os livros com quantidades")
        print("5. Sair")

        opcao = input("\nEscolha uma opção (1-5): ").strip()

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            remover_livro()
        elif opcao == "3":
            consultar_livro()
        elif opcao == "4":
            mostrar_estoque()
        elif opcao == "5":
            print("\nEncerrando o programa. Até logo!\n")
            break
        else: 
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()