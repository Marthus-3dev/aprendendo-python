sentence = input("Digite a sua frase: ").split()

counting_words ={}

for k in sentence:

    if k not in counting_words:
        counting_words[k]= 1
    else:
        counting_words[k] += 1

print(counting_words)
