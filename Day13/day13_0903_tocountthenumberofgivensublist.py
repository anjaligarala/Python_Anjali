# Task: To count the number of given sublist

'''
Output:
dict1 = {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
'''

list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]

dict1 = {}
for ele in list1:
    dict1[tuple(ele)] = list1.count(ele)
print(dict1)
