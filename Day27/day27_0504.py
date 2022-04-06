# Display all the integer within the range of 100 to 200 whose sum is even

user_input = range(100, 200)
dict01 = {}
for digit in user_input:
    count = 0
    for char in str(digit):
        count = int(char) + count
    if count % 2 == 0:
        print(digit)

'''       
output:
101
103
105
107
109
110
112
114
116
118
121
123
125
127
129
130
132
134
136
138
141
143
145
147
149
150
152
154
156
158
161
163
165
167
169
170
172
174
176
178
181
183
185
187
189
190
192
194
196
198
'''
