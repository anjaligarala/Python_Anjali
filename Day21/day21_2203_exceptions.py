try:
    a = 1 / 0

    fo = open("my_test_file_for_exception", 'w')
    fo.write("This is my test file for exception handling")

except IOError:
    print("Cant file the file or read data")

except ZeroDivisionError:
    print("Cant be divided by zero")

else:
    print("File was found and data has been written")
    fo.close()

finally:
    print("I will get executed anyway")
