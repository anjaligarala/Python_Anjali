s = input()
print(s)
inp_list = s.split(" ")
out_list = []
print(inp_list)

print(list(s))
for word in inp_list:
    if word:
        if word[0].isalpha():
            out_list.append(word.title())
        else:
            out_list.append(word)
    else:
        out_list.append(word)

print(" ".join(out_list))
