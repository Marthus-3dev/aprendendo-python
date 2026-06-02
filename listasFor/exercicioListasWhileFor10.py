import random
cpuNumber = random.randint(1,20)
userGuess = int(input("Qual número inteiro eu estou pensando de 1 a 20?\n"))
while userGuess != cpuNumber:
    if userGuess < cpuNumber:
        userGuess = int(input(f"O número {userGuess} é menor que o número que pensei. Digite outro!\n"))
    else:
        userGuess = int(input(f"O número {userGuess} é maior que o número que pensei. Digite outro!\n"))
print(f"Você acertou! Eu pensei no número {cpuNumber}!")