# from collections import Counter

no_of_shoes = int(input())
shoe_sizes = input().split()
no_of_customers = int(input())

list01 = []
for i in range(no_of_customers):
    shoe_size, price = map(int, input().split())
    list01.append((shoe_size, price))
print(list01)
