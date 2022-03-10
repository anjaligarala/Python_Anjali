# Task: print length of str from list in distionary
'''
dist ={"Anjali": [6,1,5], "Sohil": [5,1,4]}
"Anjali": [6,1,5]
6 = length of str
1 = capital letters in str
5 = small letters in str
'''

input_names = ["Anjali", "Sohil", "Vasu", "Soumya", "Sayali", "NitiN"]
output_dict = {}

for name in input_names:
    len_name = len(name)  # length of string
    fr_tmp_dict = {}
    # prints uppercase and lowercase of string
    upper_case_cnt, lower_case_cnt = 0, 0
    for char_name in name:
        list_factors, frequency_char = [], 0
        if char_name.isupper():
            upper_case_cnt = upper_case_cnt + 1
        if char_name.islower():
            lower_case_cnt = lower_case_cnt + 1
        # prints frequency of characters in string
        frequency_char = name.count(char_name)

        for facs in range(1, (frequency_char + 1)):
            if frequency_char % facs == 0:
                list_factors.append(facs)
        if char_name not in list(fr_tmp_dict.keys()):
            fr_tmp_dict[char_name] = {frequency_char: list_factors}

    # prints Yes or No if string is palindrome
    is_palindrome = "YES"
    if name != name[::-1]:
        is_palindrome = "No"

    # all output kept in dictionary
    output_dict[name] = (len_name, upper_case_cnt, lower_case_cnt, is_palindrome, fr_tmp_dict)

# print of final dictionary
print(output_dict)
