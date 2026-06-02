listGrades = []

for i in range(4):
    grade =+ float(input("Digite a nota do aluno: ").replace(",","."))
    listGrades.append(grade)
averageGrades = sum(listGrades)/len(listGrades)

if averageGrades >= 7:
    print("O aluno foi aprovado com a média de {:.2f} das notas {}".format(averageGrades,listGrades).replace(".",","))
else:
    print("O aluno ficou de recuperação com a média de {:.2f} das notas {}".format(averageGrades,listGrades).replace(".",","))