# Task: Concatenate list and string value ex:["Work1", "Work2", "Work3", "Work4"]
list01 = [1, 2, 3, 4]
string01 = "Work"

output_list = []
for list_element in list01:
    output_list.append(string01 + str(list_element))
print(output_list)
