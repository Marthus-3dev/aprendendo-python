while True:
    letter = input("Digite uma letra para saber se é Vogal ou Consoante.\nDigite [0] para sair. ").lower()
    match letter:
        case "0":
            print(f"Saindo!")
            break
        case "a"|"e"|"i"|"o"|"u":
                print("Vogal\n")
        case _:
            print("Consoante\n")