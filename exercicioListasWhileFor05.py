userPassword = "LuizinDaBetoneira67@"

userInput = input("Bem-Vindo(a) SpeedLoc.\nPor Favor digite sua senha: ")

if userInput != userPassword:

    for i in range(2,0,-1):

        print("Senha incorreta, Você tem apenas {} tentativas.".format(i))
        userInput = input("Digite a senha novamente: ")

        if userInput == userPassword:
            print("Acesso permitido, Olá Luiz")
            break

    else:
        print("Acesso negado! Sua conta foi bloqueada!")

else:
    print("Acesso permitido, Olá Luiz")