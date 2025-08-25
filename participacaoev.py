palestra_ia = set()
workshop_python = set()

def adicionar_aluno():
        nome = input("\nNome do aluno: ").strip().lower()
        while nome == "":
             print("\nO nome não pode ser nulo.\n")
             nome = input("\nNome do aluno: ").strip().lower()
             
        evento = input("\nEvento (IA ou Python): ").strip().lower()

        if evento == "ia":
             palestra_ia.add(nome)
             print(f"\n{nome} adicionado à palestra de IA.")
        elif evento == "python":
             workshop_python.add(nome)
             print(f"\n{nome} adicionado ao workshop de Python.")
        else:
             print("\nEvento inválido. Digite apenas 'IA' ou 'Python'.\n")

def mostrar_ambos():
        ambos = palestra_ia.intersection(workshop_python)
        print("\nAlunos que participaram de ambos os eventos: \n")

        if ambos:
            for aluno in ambos:
                print(aluno)
        else:
             print("\nNenhum aluno participou de ambos os eventos.\n")

            
def mostrar_so_ia():
        somente_ia = palestra_ia.difference(workshop_python)
        print("\nAlunos que participaram somente da palestra de IA: \n")

        if somente_ia:
            for aluno in somente_ia:
                print(aluno)
        else:
             print("\nNenhum aluno participou somente da palestra de IA.\n")

def mostra_pelo_menos_um():
        pelomenos_um = palestra_ia.union(workshop_python)
        print("\nAlunos que participaram de pelo menos um evento: \n")

        if pelomenos_um:
            for aluno in pelomenos_um:
                print(aluno)
        else:
             print("\nNenhum aluno participou de eventos.\n")

def verificar_participacao():
     nome = input("\nDigite o nome do aluno a verificar: ").strip()

     em_ia = nome in palestra_ia
     em_python = nome in workshop_python

     if em_ia and em_python:
          print(f"\n{nome} participou de ambos os eventos.")
     elif em_ia:
            print(f"\n{nome} participou somente da palestra de IA.")
     elif em_python:
            print(f"\n{nome} participou somente do workshop de Python.")
     else:
        print(f"\n{nome} não participou de nenhum evento.")

def main():
    while True:
        print("\n---MENU---\n")
        print("1. Adicionar aluno a um evento")
        print("2. Mostrar alunos que participaram de ambos os eventos")
        print("3. Mostrar alunos que participaram somente da palestra de IA")
        print("4. Mostrar alunos que participaram de pelo menos um evento")
        print("5. Verificar participação de um aluno")
        print("6. Sair")

        opcao = input("\nEscolha uma opção (1-6): ").strip()

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            mostrar_ambos()
        elif opcao == "3":
            mostrar_so_ia()
        elif opcao == "4":
            mostra_pelo_menos_um()
        elif opcao == "5":
            verificar_participacao()
        elif opcao == "6":
            print("\nEncerrando o programa. Até logo!\n")
            break
        else: 
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()