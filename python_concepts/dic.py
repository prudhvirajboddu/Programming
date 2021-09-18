students = {'name': 'prudhvi', 'age': 26, 'courses': ['maths', 'science']}

print(students)

print(students.get('courses'))

students.update({'phone': 885})

st1 = students.copy()

print(st1)

students.pop('name')    

for k,v in students.items():
    print(k,':',v)

print("%$$$$$")

for k,v in reversed(st1.items()):
    print(k,v)