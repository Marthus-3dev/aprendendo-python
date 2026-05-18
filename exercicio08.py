print("=====================================\nClassificação de Atletas por Categoria")
age = int(input("Digite a sua idade: "))

if age <= 9:
    print("Você é um atleta mirin ({} Anos)".format(age))
elif age <= 14:
    print("Você é um atleta Infantil ({} Anos)".format(age))
elif age <= 19:
    print("Você é um atleta Junior ({} Anos)".format(age))
elif age <=25:
    print("Você é um atleta Sênior ({} Anos)".format(age))
else:
    print("Você é um atleta Master ({} Anos)".format(age))