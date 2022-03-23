n = int(input("Enter no"))
arr = list(map(int, input("Enter the list ele").split()))

list01 = sorted(arr, reverse=True)
print(list01)

max_ele = list01[0]

for ele in list01:
    if ele < max_ele:
        print(ele)
        break

'''
psuedo code:
1 - Sort the input list in decending order and store in a variable.
2 - Find the max value in the sorted list variable.
3 - iterate over the sorted list and find the second highest

'''
