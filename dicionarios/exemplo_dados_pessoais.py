personal_data = {
    "nome" : "Luiz",
    "idade" : 19,
    "nascimento" : "16-11-2006",
    "sexo" : "M",
    "altura" : 1.80,
    "temCNH" : False
}

personal_data["altura"] = 1.79
personal_data["peso"] = 70 #adiciona chaves e dados
personal_data.pop("idade") #remove o item

resume = "s"
while resume == "s":
    new_key, new_data = input()

