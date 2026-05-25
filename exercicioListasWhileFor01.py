listNumbers = []

for i in range(6):
    number =+ int(input("Digite um número inteiro: "))
    listNumbers.append(number)

print("Os números inteiros ditados foram:{}".format(listNumbers))
print("A soma dos números inteiros é: {} ".format(sum(listNumbers)))
print("O maior número inteiro da lista é: {}".format(max(listNumbers)))
print("O menor número inteiro da lista é: {}".format(min(listNumbers)))
