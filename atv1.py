alunos = []
medias_alunos = []

while True:
    print("\nMENU")
    print("1 - Cadastrar aluno")
    print("2 - Mostrar alunos")
    print("3 - Remover aluno")
    print("4 - Relatório da turma")
    print("5 - Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        nome = input("Nome do aluno: ")

        if nome in alunos:
            print("Esse aluno já está cadastrado.")
        else:
            notas = []

            for i in range(3):
                nota = float(input(f"{i+1}ª nota: "))

                while nota < 0 or nota > 10:
                    print("Nota inválida! Digite de 0 a 10.")
                    nota = float(input(f"{i+1}ª nota: "))

                notas.append(nota)

            media = sum(notas) / 3

            alunos.append(nome)
            medias_alunos.append(media)

            if media >= 6:
                print("Aprovado!")
            else:
                print("Reprovado!")

    elif escolha == 2:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("\nLISTA DE ALUNOS")

            for i in range(len(alunos)):
                if medias_alunos[i] >= 6:
                    situacao = "Aprovado"
                else:
                    situacao = "Reprovado"

                print(f"{alunos[i]} - média {medias_alunos[i]:.1f} - {situacao}")

    elif escolha == 3:
        nome = input("Nome do aluno para remover: ")

        if nome in alunos:
            pos = alunos.index(nome)
            alunos.pop(pos)
            medias_alunos.pop(pos)
            print("Aluno removido.")
        else:
            print("Aluno não encontrado.")

    elif escolha == 4:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            total = len(alunos)
            aprovados = 0
            reprovados = 0
            soma = 0

            maior = medias_alunos[0]
            menor = medias_alunos[0]
            aluno_maior = alunos[0]
            aluno_menor = alunos[0]

            for i in range(len(alunos)):
                soma += medias_alunos[i]

                if medias_alunos[i] >= 6:
                    aprovados += 1
                else:
                    reprovados += 1

                if medias_alunos[i] > maior:
                    maior = medias_alunos[i]
                    aluno_maior = alunos[i]

                if medias_alunos[i] < menor:
                    menor = medias_alunos[i]
                    aluno_menor = alunos[i]

            print("\nRELATÓRIO FINAL")
            print("Total de alunos:", total)
            print("Aprovados:", aprovados)
            print("Reprovados:", reprovados)
            print(f"Média da turma: {soma/total:.1f}")
            print("Maior média:", aluno_maior)
            print("Menor média:", aluno_menor)

    elif escolha == 5:
        print("Sistema encerrado")
        break

    else:
        print("Opção inválida.")



