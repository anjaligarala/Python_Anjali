user_input = [[1,2,3],[4,5,6],[10,11,12],[7,8,9]]

'''
for sum_list in user_input:  
    sum(sum_list)
    if sum(sum_list) > max(sum_list):
     print(sum_list)
'''
'''
sum_list = []
for list_index in range(len(user_input)):
    sum_list.append(sum(user_input[list_index]))
print(user_input[sum_list.index(max(sum_list))])
'''

for list_index1 in range(len(user_input)):
    for list_index2 in range(list_index1 + 1, len(user_input)):
        if sum(user_input[list_index2]) > sum(user_input[list_index1]):
            user_input[list_index1], user_input[list_index2] = user_input[list_index2], user_input[list_index1]

print(user_input[-1])