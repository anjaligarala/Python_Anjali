student_info = [{"id": 1, "name": 'Anjali', "class": 5}, {"id": 2, "name": 'Sohil', "class": 6},
                {"id": 3, "name": 'Soumya', "class": 7}]
# [[1,Anjali,5][2,Sohil,6][3,Soumya,7]]

student_info_output = []
for student in student_info:
    convert = list(student.values())
    student_info_output.append(convert)
print(student_info_output)
