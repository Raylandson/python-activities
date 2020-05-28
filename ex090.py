"""l = []
people = {'name': 'gustavo', 'sex': 'M', 'age': 22}
print(f"the {people['name']} is {people['age']} years old")
l.append(people.copy())
del people['sex']
l.append(people.copy())
print(l)
"""
student = dict()
student['name'] = str(input('what is the student name? '))
student['average'] = float(input('what is the student average? '))
if student['average'] >= 7:
    student['situation'] = 'okay'
else:
    student['situation'] = 'failed'
for k, v in student.items():
    print(f"he {k} is {v}")
    