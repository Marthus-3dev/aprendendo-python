listaIdades = []
for i in range (10):
    idade = int(input("Digite sua idade:"))
    listaIdades.append(idade)

print("------------------------------")
print("Imprimindo idade uma abaixo da outra:")
listaIdades.sort()

for i in listaIdades:
    print(i)