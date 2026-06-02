while True:
    grade = float(input("Digite a nota do aluno ( 0.1 - 10)\nDigite [0] para sair: "))
    match grade:
        case 0:
            print("Saindo....")
            break
        case grade if grade >= 7.5 and grade <= 10:
            print("O aluno tirou nota A!\nExcelente trabalho!")
        case grade if grade < 7.5 and grade > 5:
            print("O aluno tirou nota B.\nBom desempenho.")
        case grade if grade >= 5:
            print("O aluno tirou nota C.\nSatisfatório.")
        case grade if grade < 5 and grade > 2.5:
            print("O aluno tirou nota D.\nAbaixo da média. [ATENÇÃO]")
        case grade if grade <= 2.5:
            print("O aluno tirou nota F!\nReprovado.")
        case _:
            print("Nota incoerente! Escolha um número de 0.1 a 10.\n\n")