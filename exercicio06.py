side1 = float(input("Digite o primeiro lado do triângulo em centímetros: ").replace(",","."))
side2 = float(input("Digite o segundo lado do triângulo em centímetros: ").replace(",","."))
side3 = float(input("Digite o terceiro lado do triângulo em centímetros: ").replace(",","."))

if side1+side2 < side3 or side1+side3 < side2 or side3+side2 < side1:
    print("Os valores informados não formam um triângulo")
else:
    if side1 == side2 == side3:
        print("Este triângulo é equilátero.")
    elif side1 != side2 !=side3:
        print("Este triângulo é escaleno.")
    else:
        print("Este triângulo é isósceles")