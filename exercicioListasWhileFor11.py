bankNotes = [50,20,10,5,2]

withdraw = int(input("Digite a quantia para sacar: "))

while withdraw != 0:
    if withdraw >= 50:
        withdraw /= 50
        change = withdraw % 50
    elif withdraw >= 20:
        withdraw /= 50
