import pandas

student_dict = {
    "student": ["Alex", "Adjoa", "Ama"],
    "score": [90, 50, 60]
}

for (key,value) in student_dict.items():
    print(key)
    print(value)
student_data_frame = pandas.DataFrame(student_dict)
# for (key, value) in student_data_frame.items():
#     print(value)
# print(student_data_frame)
#loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    if row.student == "Ama":
        print(row.score)
