import re

no_of_inputs = int(input())
phone_number = []
for i in range(1, no_of_inputs + 1):
    phone_number.append(input())

for j in phone_number:
    if re.search("^[789][0-9]{9}$", j):
        print("Yes")
    else:
        print("No")
