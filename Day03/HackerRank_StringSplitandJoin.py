
'''
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
Example:
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:
>>> a = "-".join(a)
>>> print a
this-is-a-string 
'''

def split_and_join(line):
    # write your code here
    name = line.split(" ")
    name = "-".join(name)
    return name

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)