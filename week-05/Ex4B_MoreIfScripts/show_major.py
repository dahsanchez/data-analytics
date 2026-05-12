student_name = 'Dahlia'
student_major = 'CSCI'

if student_major == 'BIOL':
    name = 'Biology'
    building = 'Science Blgd, Room 310'
elif student_major == 'CSCI':
    name = 'Computer Science'
    building = 'Sheppard Hall, Room 314'
elif student_major == 'ENG':
    name = 'English'
    building = 'Kerr Hall, Room 201'
elif student_major == 'HIST':
    name = 'History'
    building = 'Kerr Hall, Room 114'
elif student_major == 'MKT':
    name = 'Marketing'
    building = 'Westly Hall, Room 310'
else:
    name = 'unknown'
    building = ''

print(f"""
Student Name: {student_name}
Major: {student_major} {name}
Building: {building}
""")