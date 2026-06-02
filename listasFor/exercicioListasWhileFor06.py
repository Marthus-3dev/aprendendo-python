listEmails = ["joao@gmail.com", "maria@senac.df", "pedro@outlook.com", "ana@senac.df"]
listSenacEmails = []

for i in listEmails:

    if i.endswith("@senac.df"):
        listSenacEmails.append(i)

print(listSenacEmails)