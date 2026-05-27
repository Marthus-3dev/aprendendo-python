userGrade = float(input("Digite a nota do aluno (de 0 a 10): ").replace(",","."))

while userGrade < 0 or userGrade > 10:
    userGrade = float(input("Valor inválido! \nDigite uma nota de 0 a 10: ").replace(",","."))

print(f"A nota do aluno é: {userGrade}".replace(".",","))