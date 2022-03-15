# write a function to check if string is palidrome or not

def palidrome_string(name):
    for stingname in name:
        if name == name[::-1]:
            return True
        else:
            return False


a = palidrome_string("nitin")
print(a)
