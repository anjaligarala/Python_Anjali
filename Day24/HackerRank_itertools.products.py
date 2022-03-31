from itertools import product

A = map(int, input().strip().split())
B = map(int, input().strip().split())

for i in product(A, B):
    print(i, end=" ")
