#Questão 2
x = 1 
while x <4:
    x = x + 1 
print(x)

#Questão 3
numbers = [1,2,3,4,5]
pairs = []
for n in numbers:
    if n % 2 == 0:
        pairs.append(n)
print(pairs)

#Questão 5
for i in range(1,5):
    if i == 3:
        continue
    print(i, end=" ")

#Questão 6
factor = 1 
list = [1,2,3,4]
for x in list:
    if x > 2:
        factor = factor * x
print(factor)

#Questão 7
itens = ["a", "b"]
result = []
for i in itens:
    for j in [1,2]:
        result.append(i + str(j))
print(result)

#Questão 8
names = ["Carol", "Lucas", "Mari"]
found = False
for n in names:
    if n == "Lucas":
        found = True
print(found)

#Questão 9
energy = 10
steps = 0
while energy > 0:
    steps = steps + 2
    energy = energy - 3
print(steps)

#Questão 10
list2 = [1,2,3,4,5]
list2.pop(1)
list2.append(-1)
list2.sort(reverse=int)
print(list2)