listYearOfBirth = []
listOverage = []
listUnderage = []

print("=-=-=-=-=Calculador de Maioridade=-=-=-=-=")

for i in range(7):
    yearOfBirth =+ int(input("Digite o ano de nascimento do aluno: "))
    listYearOfBirth.append(yearOfBirth)
    if 2026 - yearOfBirth >= 18:
        listOverage.append(yearOfBirth)
    else:
        listUnderage.append(yearOfBirth)
print("Os anos de nascimento digitados dos alunos são: \n{}".format(listYearOfBirth))
print("\nOs alunos que tem maioridade são: \n{}".format(listOverage))
print("\nOs alunos que ainda são menores:\n{}".format(listUnderage))