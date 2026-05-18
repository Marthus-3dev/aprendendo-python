print("Calculadora BlackFriday!!!")
purchaseValue = float(input("Digite o valor total de suas compras: "))

if purchaseValue <=100:
    print("Sua compra teve o valor de {}\n Você precisa de um valor superior à R$100,00 em compras.".format(purchaseValue))

elif purchaseValue > 100 and purchaseValue <= 300:
    saleFivePercent = purchaseValue * 0.05
    purchaseValue -= saleFivePercent
    print("A sua compra apos o desconto de 5% (-{:.2f}) ficou com o valor de R${:.2f}".format(saleFivePercent,purchaseValue))

elif purchaseValue > 300 and purchaseValue <= 500:
    print("A sua compra apos o desconto de 10% (-{:.2f}) ficou com o valor de R${:.2f}".format(purchaseValue*0.1,purchaseValue*0.9))

else:
    print("A sua compra apos o desconto de 15% (-{:.2f}) ficou com o valor de R${:.2f}".format(purchaseValue*0.15,purchaseValue*0.75))