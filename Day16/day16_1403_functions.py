'''
input_name = "Anjali"

def find_length(input_name):
    output = len(input_name)
    print(output)
find_length("Anjali")
'''

'''
def changename(list01):
    list01.append(4)
    print(list01)

changename([1, 2, 3])
'''
# Required arguments
'''
def printme(name,age):
    print(name + str(age))
printme("Anjali", 12)
'''

# keyword arguments
'''
def printme(name, age):
    print(name + str(age))
printme(name = "Anjali", age = 28)
'''
# default arguments
'''
def printme(name, age = 28):
    print(name + str(age))
printme(name = "Anjali", age = 30)
printme(name = "Anjali")
'''

# Variable-length arguments
'''
def printme(arg1, *vartuple): # *vartuple --> positional argument
    print(arg1)
    print(vartuple)
    for abc in vartuple:
        print(abc)
printme(10, 40, 30, 50)
'''

'''
def printme(arg1, **kwrarg): # **kwrarg --> keyword argument
    print(arg1)
    print(kwrarg)

    for abc in kwrarg:
        print(kwrarg[abc])
printme(10, name = "Anjali", age = 28)
'''


def printme(*posarg, **kwrarg):
    for abc in posarg:
        print(abc)

    for xyz in kwrarg:
        print(kwrarg[xyz])


printme(10, 20, 30, name="Anjali", age=28)
