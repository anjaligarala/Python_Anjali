'''
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    N = int(input())
    list_input = []
    
    for i in range(N):
        user_input = input()
        cmd_ops = user_input.split()
        if cmd_ops[0] == 'insert':
            list_input.insert(int(cmd_ops[1]),int(cmd_ops[2]))
        if cmd_ops[0] == 'append':
            list_input.append(int(cmd_ops[1]))
        if cmd_ops[0] == 'remove':
            list_input.remove(int(cmd_ops[1]))
        if cmd_ops[0] == 'pop':
            list_input.pop()
        if cmd_ops[0] == 'sort':
            list_input.sort()
        if cmd_ops[0] == 'reverse':
            list_input.reverse()
        if cmd_ops[0] == 'print':
            print(list_input)