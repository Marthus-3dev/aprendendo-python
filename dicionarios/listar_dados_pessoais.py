personal_data = {
    "nome" : "Luiz",
    "idade" : 19,
    "nascimento" : "16-11-2006",
    "sexo" : "M",
    "altura" : 1.79,
    "temCNH" : False
}

print(personal_data)

for key,data in personal_data.items():
    if key == "idade" and data >= 18:
        print("Maior de idade")
    print(f"{key} : {data}")
