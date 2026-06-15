person = {
    "nome" : "Renan Santos",
    "idade" : 42,
    "cidade" : "São Paulo"
}
for k,v in person.items():
    print(f"{k} : {v}")
print("==========================")
person["profissao"] = "Empresario"
for k,v in person.items():
    print(f"{k} : {v}")