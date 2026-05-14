num1 = float(input("Digite o primeiro número para comparar: ").replace(",","."))
num2 = float(input("Digite o segundo número para comparar: ").replace(",","."))

if num1 > num2:
    print("O número {} é maior que o número {}!".format (num1,num2).replace(".",","))
elif num1 < num2:
    print("O número {} é maior que o número {}!".format(num2,num1).replace(".",","))
else:
    print("Os números {} e {} são iguais!".format(num1,num2).replace(".",","))