salary = float(input("Digite o seu salário: "))
monthlyDesiredPayments = float(input("Digite o valor desejado da parcela: "))

maxMonthlyDesiredPayments = salary*0.3
if maxMonthlyDesiredPayments <= monthlyDesiredPayments:
    print("Seu crédito esta com valor acima de 30%({:.2f}) do seu salario!\n  Diminua o valor da sua parcela desejada! ({:.2f})".format(maxMonthlyDesiredPayments))
else:
    print("O seu crédito foi aprovado!")