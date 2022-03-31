s = input()
'''
if s.isalnum():
    print(True)
else:
    print(False)

if s.isalpha():
    print(True)
else:
    print(False)

if s.isdigit():
    print(True)
else:
    print(False)

if s.islower():
    print(True)
else:
    print(False)

if s.isupper():
    print(True)
else:
    print(False)
'''

bool_dict = {'alnum_cnt': 0, 'alpha_cnt': 0, 'digit_cnt': 0, 'lwrcase_cnt': 0, 'uprcase_cnt': 0}
for char in s:
    if char.isalnum():
        bool_dict['alnum_cnt'] = bool_dict['alnum_cnt'] + 1
    if char.isalpha():
        bool_dict['alpha_cnt'] = bool_dict['alpha_cnt'] + 1
    if char.isdigit():
        bool_dict['digit_cnt'] = bool_dict['digit_cnt'] + 1
    if char.islower():
        bool_dict['lwrcase_cnt'] = bool_dict['lwrcase_cnt'] + 1
    if char.isupper():
        bool_dict['uprcase_cnt'] = bool_dict['uprcase_cnt'] + 1

for key, value in bool_dict.items():
    if value > 0:
        print(True)
    else:
        print(False)
