n1 = int(input("digite o primeiro número:"))
n2 = int(input("digite o segundo número:"))

result = n1 // n2
result2 = n1 % n2
result3 = n1 ** n2

print("a divisão inteira é {} o resto é {} \n a potencia é {} ".format(result,result2,result3))

print("-----------------------------")
print("|   OPERADORES RELACIONAIS  |")
print("-----------------------------")

relac1 = n1 > n2
relac2 = n1 < n2
relac3 = n1 >= n2
relac4 = n1 <= n2
relac5 = n1 == n2
relac6 = n1 != n2

print("Os resultados das relações estarão abaixo:\n{} \n{} \n{} \n{} \n{} \n{}".format(relac1,relac2,relac3,relac4,relac5,relac6))