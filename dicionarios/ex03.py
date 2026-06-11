
squares_dictionary = {}

for i in range(1,6):
    squares_dictionary.setdefault(i, i**2)
for k,v in squares_dictionary.items():
    print(f"{k}² = {v}")
