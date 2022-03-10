# Task: print multiple list in one single list
'''
output:
list2 = [1,2,3,4,5,6,7,8,9,10,11,12]
'''

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

list2 = []
for ele in list1:
    list2.extend(ele)
print(list2)
