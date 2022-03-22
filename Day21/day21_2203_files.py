fo = open('my_test_file.txt', 'a')
# mode w = write mode and overwrites the objects
# mode a = appends the objects in  file
for file_input in range(10, 20):
    fo.write("My Name is Anjali and I am learning python" + str(file_input) + "\n")
fo.close()
