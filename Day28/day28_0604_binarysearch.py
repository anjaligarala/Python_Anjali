# Write a program to implement binary search and find the position of the no

def binary_search(n, target):
    start_index, end_index = 0, len(n) - 1
    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index) // 2
        if list01[mid_index] > target:
            end_index = mid_index
        elif list01[mid_index] < target:
            start_index = mid_index
        else:
            return mid_index


n = [4, 2, 7, 1, 8, 3, 6]
target = int(input())
n.sort()
print(n)
