# Task : Print square of keys ex: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

number_square = int(input("Enter your input:"))
square_dict_output = {}

for element in range(1, number_square):
    square_dict_output[element] = element * element
print(square_dict_output)
