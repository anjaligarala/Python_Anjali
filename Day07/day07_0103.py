user_input = input("Enter your input - ")

convert_list = user_input.split(" ")
print(convert_list)

for check_element in convert_list:
    if len(check_element) >= 2:       
        if check_element[0] == check_element[-1]:
            print(check_element)
