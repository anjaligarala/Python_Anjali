dict01 = {"1": ["A", "B"], "2": ["C", "D"]}

'''
Output:
AC
AD
BC
BD
'''

list_dict = list(dict01.values())
print(list_dict)

for list01_ele in list_dict[0]:
    for list02_ele in list_dict[1]:
        print(list01_ele + list02_ele)
