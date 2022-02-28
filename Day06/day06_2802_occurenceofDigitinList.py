user_input01 = input("Enter input - ").split(" ")
print(user_input01)

#convert string into int list
for i in range(len(user_input01)):
    user_input01[i] = int(user_input01[i])
print(user_input01)

#find the occurence of digit in list
count = 0
user_input02 = int(input("Enter your second input - "))
for list_value in user_input01:
    if list_value == user_input02:
        count = count + 1
print(count)

'''
Output:
Enter input - 11 11 23 11 23
['11', '11', '23', '11', '23']
[11, 11, 23, 11, 23]
Enter your second input - 11
3
'''



    



