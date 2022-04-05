dist01 = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

# output {65 : 'A', 66 : 'B', 67 : 'C', 68 :'D'}

dist02 = {}
for key, value in dist01.items():
    dist02[value] = key

print(dist02)
