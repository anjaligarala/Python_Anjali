# Task: Check if your key is present in Dictionary

dist01 = {"Name": "Anjali", "Age": 28, "City": "PUNE"}
user_input = input("Enter key you want to search:")
'''
for key in dist01:
    if user_input == key:
        print("Key is present")
    else:
        print("Key is not present")
'''

print(user_input in dist01)
