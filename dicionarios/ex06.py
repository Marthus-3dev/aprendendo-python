stock = {
    "Teclado" : 15,
    "Mouse" : 22,
    "Monitor" : 8
}
for k, v in stock.items():
    print(f"{k} : {v}")
update_stock = False
procede = "s"
while procede == "s":
    product, quantity = input("Escolha o nome do produto e a quantidade desejada separada por vírgula: ").split(",")

    for key, value in stock.items():
        if value == 0:
            print("Produto sem estoque!")
            continue
        if value < int(quantity):
            print("Você escolheu uma quantidade maior do que há no estoque!!")
            continue
        else:
            stock[key] -= int(quantity)
            update_stock  = True
    if update_stock:
        print("Estoque atualizado!")
        for key, value in stock.items():
            print(f"{key} : {value}")
    procede = input("Deseja continuar? s/n: ")[0].lower()