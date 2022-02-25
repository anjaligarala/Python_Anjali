user_input = input("Enter your value - ")
smallest_no = 0


list_no = user_input.split(" ")
for i in range(0,len(list_no)):
    list_no[i] = int(list_no[i])

for i in list_no:
    if i == min(list_no):
        smallest_no = i
        print(smallest_no)