# Task: Check if dictionary is empty

list01 = [{}, {}, {}, {"key": "Name"}, {}, {}]
is_empty = True

for element in list01:
    if element:
        is_empty = False
        break

if is_empty == True:
    print("Element is not present in Dictionary")
else:
    print("Element is present in Dictionary")
