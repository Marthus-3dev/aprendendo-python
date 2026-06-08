list_stock = [
    [12, 5, 8],

    [3, 15, 2],

    [19, 0, 7]
]

shelf, partition = input(f"Digite o número da prateleira (1 a 3) e da divisória (1 a 3) separado por vírgula:").split(",")

print(f"A quantidade de caixas na prateleira {shelf} na divisória {partition} é : {stock[int(shelf) -1 ][int(partition) -1 ]}")