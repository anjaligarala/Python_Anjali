user_input = [[1,2,3],[4,5,6],[10,11,12],[7,8,9]]

for sum_list in user_input:  
    sum(sum_list)
    if sum(sum_list) > max(sum_list):
     print(sum_list)

