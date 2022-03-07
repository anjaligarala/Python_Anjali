dist01 = {"V": 10, "VI": 10, "VII": 40, "VIII": 20, "IX": 70, "X": 80, "XI": 40, "XII": 20}
convert_dist_list = list(dist01.values())
print(convert_dist_list)
result = {}

for value in convert_dist_list:
    result[value] = convert_dist_list.count(value)
print(result)
