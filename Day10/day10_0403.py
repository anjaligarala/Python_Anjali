dict_list = {"Name": "Anjali", "Age": 28, "City": "Pune"}

# .items() --> Prints Key and value of dict_list
# for key, value in dict_list.items():
# print(key, value)

# .keys() --> Prints Key of dict_list
# for key in dict_list.keys():
#     print(key, dict_list[key])
# output
# Name Anjali
# Age 28
# City Pune

# .items() --> Prints Key and value of dict_list
for key in dict_list:
    print(key, dict_list[key])
