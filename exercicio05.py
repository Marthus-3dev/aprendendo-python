mass = float(input("Digite o seu peso em Quilogramas: ").replace("kg""KG""Kg",""))
height = float(input("Digite a sua altura em metros: ").replace(",","."))

bmi = mass/(height**2)

if bmi <= 18.5:
    print("Você está abaixo do peso e com o IMC de ", bmi)
elif bmi <= 24.99:
    print("Você está com o peso normal e com o IMC de ", bmi)
elif bmi <= 29.99:
    print("Você esta sobrepeso e com o IMC de ", bmi)
else:
    print("Você esta obeso e com o IMC de ", bmi)
