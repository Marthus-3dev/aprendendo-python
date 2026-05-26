listNumbers = []
listOdds = []
listPairs = []

for i in range(10):
    number =+ int(input("Digite um número inteiro: "))
    if number % 2 == 0:
        pair =+ number
        listPairs.append(pair)
    else:
        odd =+ number
        listOdds.append(odd)
    listNumbers.append(number)
print("Os números inteiros digitados são: \n{}".format(listNumbers))
print("\nOs Números inteiros pares são: \n{}".format(listPairs))
print("\nOs números inteiros impares são:\n{}".format(listOdds))