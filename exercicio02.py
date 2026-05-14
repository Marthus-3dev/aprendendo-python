number = float(input("Digite um número para descobrir se é par ou impar:").replace(",","."))
rest = number % 2

if rest == 0:
    print("O número é Par!")
else:
    print("O número é impar!")