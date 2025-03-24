Aluno = input("Digite o nome do aluno: ")
turno = input("Turno de Aula: \n" + "M-Matutino\n" + "V-Vespertino\n" + "N-Noturno\n")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

match turno:
    case "M":
        print("Estuda no Matutino")
    case "V":
        print("Estuda no Vespertino")
    case "N":
        print("Estuda no Noturno")
    case   _:
        print("Inexistente")

if media < 3:
    print("Reprovado")
elif media >= 7 and media < 7:
    print("Recuperação")
elif media >= 7 and media < 9:
    print("Aprovado")
else:
    print("Aprovado ccom louvor!")

print(f"""
                        *   *   *   *   *   *   *   *   *
                        *             {Aluno}              *
                        *                               *
                        *               {turno}             *
                        *                               *
                        *       Media de notas {media}      *
                        *   *   *   *   *   *   *   *   *

""")