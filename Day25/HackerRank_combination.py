from itertools import combinations

S, k = input().split()

for j in sorted(S):
    print("".join(j))

for i in list(combinations(sorted(S), int(k))):
    print("".join(i))
