# Write a program to implement liner search and find the position of the no
import time
import datetime

list01 = list(range(1000))
user_input = int(input())
start_time = datetime.datetime.now()

for ele in range(len(list01)):
    if list01[ele] == user_input:
        print(ele, user_input)
        end_time = datetime.datetime.now()
        print("Your algorithm took " + str((end_time - start_time).total_seconds()))
        exit()

print("Element not found")
end_time = datetime.datetime.now()
print("Your algorithm took " + str((end_time - start_time).total_seconds()))
