fo = open("my_test_file.txt", 'r')
var = fo.readlines()
fo.close()

fo1 = open("my_test_file.txt", 'w+')
for convert_string in var:
    fo1.write(convert_string.upper())
fo1.close()
