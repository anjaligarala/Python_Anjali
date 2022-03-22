fo = open("my_test_file.txt", 'r')

var = fo.readline()
while var:
    var = fo.readline()
    print(var)
