list_square_matrix = [
    [5, 2, 9],
    [1, 8, 3],
    [4, 7, 6]
]
list_numbers = []

for i in range(len(list_square_matrix)):
    list_numbers .append(list_square_matrix[i][i])

print(f"A soma da diagonal da matriz é {" + ".join(map (str,list_numbers)) } = {sum(list_numbers)}")