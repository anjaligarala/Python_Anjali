user_input = input("Enter your value - ")
count = 0
output_list = []
sum_count = user_input.split(" ")
for i in sum_count:
    count = 0 
    for j in i:   
        count = int(j) + count
    output_list.append(count)
print(output_list) 




