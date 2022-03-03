user_input01 = ['a', 'b', 'c', 'd']
user_input02 = ['e', 'f', 'g', 'h']
sum = 0
list_element = []

for con_element01 in range(len(user_input01)):
    for con_element02 in range(len(user_input02)):
        if con_element01 == con_element02:
            sum = user_input01[con_element01] + user_input02[con_element02]
            list_element.append(sum)
print(list_element)
