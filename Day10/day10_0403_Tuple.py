tuple01 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2, 2, 4, 4, 4, 4, 8, 8, 8)
# print(len(tuple01))
dict01 = {}
for element_count in tuple01:
    dict01[element_count] = tuple01.count(element_count)
print(dict01)

from collections import Counter
