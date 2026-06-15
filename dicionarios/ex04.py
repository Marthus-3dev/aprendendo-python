products_dictionary = {
    "Placa de vídeo" : 2000,
    "Xbox Series X" : 5600,
    "Monitor Gamer" : 750
}

user_input = input("Digite o nome do produto à encontrar: ")
print(products_dictionary.get(user_input , "Produto não encontrado!"))








