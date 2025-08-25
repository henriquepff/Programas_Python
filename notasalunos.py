notas = []

def adicionar_nota():
    nome = input("\nNome do aluno: ").strip()
    while nome == "":
        print("\nO nome não pode estar vazio.\n")
        nome = input("\nNome do aluno: ").strip()


    nota = input("\nNota do aluno (0 a 10): ").strip()
    while not nota.replace(".", "").isdigit() or not (0 <= float(nota) <= 10):
        print("\nNota inválida. Digite um número entre 0 e 10.\n")
        nota = input("\nNota do aluno (0 a 10): ").strip()

    disciplina = input("\nDisciplina: ").strip()
    while disciplina == "":
        print("\nA disciplina não pode estar vazio.\n")
        disciplina = input("\nDisciplina: ").strip()

    notas.append((nome,nota,disciplina))
    print("\nNota adicionada com sucesso.\n")

def melhor_disciplina():
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada.\n")
        return
    
    disciplinas = []

    for n in notas:
        if n[2] not in disciplinas:
            disciplinas.append(n[2])

    print("\nMelhor aluno por disciplina: \n")

    for d in disciplinas:
        melhor_nota = -1
        melhor_aluno = ""
        for n in notas:
            if n[2] == d and float(n[1]) > float(melhor_nota):
                melhor_nota = n[1]
                melhor_aluno = n[0]
        print(f"{d}: {melhor_aluno} ({melhor_nota})")

def consultar_aluno():
    nome_busca = input("\nDigite o nome do aluno: ")
    encontrou = False

    for n in notas:
        if n[0].lower() == nome_busca.lower():
            encontrou = True
            print(f"{n[2]}: {n[1]}")

    if not encontrou:
        print("\nNenhuma nota encontrada para este aluno.\n")

def obter_nota(tupla):
    return tupla[1]

def exibir_ordenadas():
      if len(notas) == 0:
        print("\nNenhuma nota cadastrada.\n")
        return
      
      ordenadas = sorted(notas, key=obter_nota, reverse=True)

      print("\nNotas ordenadas (decrescente): \n")

      for n in ordenadas:
          print(f"{float(n[1]):.2f}, {n[0]}, {n[2]}")



def main():
    while True:
        print("\n---MENU DE NOTAS---\n")
        print("1. Adicionar nota")
        print("2. Mostrar melhor aluno por disciplina")
        print("3. Consultar notas por aluno")
        print("4. Exibir notas ordenadas (decrescente)")
        print("5. Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "1":
            adicionar_nota()
        elif opcao == "2":
            melhor_disciplina()
        elif opcao == "3":
            consultar_aluno()
        elif opcao == "4":
            exibir_ordenadas()
        elif opcao == "5":
            print("\nEncerrando o programa. Até logo!\n")
            break
        else: 
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()