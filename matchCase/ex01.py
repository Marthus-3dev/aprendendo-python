while True:
    weekDay = int(input("Digite um dia da semana de 1 à 7(digite 0 para sair): "))
    match weekDay:
        case 0:
            print("Saindo....")
            break
        case 1:
            print("\nDomingo\n")
        case 2:
            print("\nSegunda\n")
        case 3:
            print("\nTerça\n")
        case 4:
            print("\nQuarta\n")
        case 5:
            print("\nQuinta\n")
        case 6:
            print("\nSexta\n")
        case 7:
            print("\nSábado\n")
        case _:
            print("Número inválido!!\nDigite um número de 1 a 7!!!\n\n")