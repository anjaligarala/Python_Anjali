user_input01 = input("Enter input - ").split(" ")
print(user_input01)
list_digit = []
list_char = []

for list_element in user_input01:
    if list_element.isdigit():
        list_digit.append(list_element)
        
    if list_element.isalpha():
        list_char.append(list_element)

print(list_digit)
print(list_char)
