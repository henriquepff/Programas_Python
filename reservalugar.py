assentos = [False] * 10

def reservar_assento():
    numero = int(input("\nDigite o número do assento para reservar (1 a 10): "))

    if 1 <= numero <= 10:
        if assentos[numero - 1] == False:
            assentos[numero - 1] = True
            print(f"\nAssento {numero} reservado com sucesso.\n")
        else:
            print(f"\nAssento {numero} já está ocupado.\n")
    else:
        print("\nNúmero de assento inválido!\n")

def liberar_assento():
    numero = int(input("\nDigite o número do assento para liberar (1 a 10): "))

    if 1 <= numero <= 10:
        if assentos[numero - 1] == True:
            assentos[numero - 1] = False
            print(f"\nAssento {numero} liberado com sucesso.\n")
        else:
            print(f"\nO Assento {numero} já está livre.\n")
    else:
        print("\nNúmero de assento inválido!\n")

def mostrar_mapa():
    print("\nMapa de Ocupação dos Assentos: \n")
    for i in range(10):
        if assentos[i] == True:
            status = "Ocupado"
        else:
            status = "Livre"
        print(f"Assento {i + 1}: {status}")
    print()


def main():
    while True:
        print("\n---Menu do Cinema---\n")
        print("1. Reservar um assento")
        print("2. Liberar um assento")
        print("3. Mostrar mapa de ocupação")
        print("4. Sair")

        opcao = input("\nEscolha uma opção (1-4): ")

        if opcao == "1":
            reservar_assento()
        elif opcao == "2":
            liberar_assento()
        elif opcao == "3":
            mostrar_mapa()
        elif opcao == "4":
            print("\nEncerrando o programa. Até logo!\n")
            break
        else: 
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()