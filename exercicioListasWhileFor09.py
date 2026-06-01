while True:
    print("Escolha a operação desejada: ")
    userChoice = int(input("[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir\n[5] Sair\n"))
    if userChoice == 1:
        number1 = float(input("Digite o primeiro número a somar: "))
        number2 = float(input("Digite o segundo número a somar: "))
        print(f" {number1} + {number2} = {number1+number2}")
    elif userChoice == 2:
        number1 = float(input("Digite o primeiro número a subtrair: "))
        number2 = float(input("Digite o segundo número a subtrair: "))
        print(f"{number1} - {number2} = {number1-number2} ")
    elif userChoice == 3:
        number1 = float(input("Digite o primeiro número a multiplicar: "))
        number2 = float(input("Digite o segundo número a multiplicar: "))
        print(f"{number1} x {number2} = {number1*number2}")
    elif userChoice == 4:
        number1 = float(input("Digite o dividendo: "))
        number2 = float(input("Digite o divisor: "))
        if number2 == 0 :
            print("Não é possível dividir por Zero!")
            continue
        print(f"{number1} / {number2} = {number1/number2}")
    else:
        print("Adeus!!")
        break