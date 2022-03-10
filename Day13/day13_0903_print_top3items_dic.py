# Task: Print top 3 items values from dictionary
'''
ex:
'Item4' 55
'Item1' 45.50
'Item3' 41.30
'''

dic1 = {'Item1': 45.50, 'Item2': 35, 'Item3': 41.30, 'Item4': 55, 'Item5': 24}

sorted_list = sorted(list(dic1.values()), reverse=True)
print(sorted_list)

for ele in range(3):
    for key in dic1:
        if sorted_list[ele] == dic1[key]:
            print(key, sorted_list[ele])
