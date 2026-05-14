dateOfBirth = int(input("Digite o seu ano de nascimento: \n"))
age = 2026 - dateOfBirth

if age < 18:
    print("Você tem", age, " anos e é menor de idade. ")
elif age < 60:
    print("Você tem", age, "anos e é adulto.")
else:
    print("Você tem", age, "anos e é idoso.")