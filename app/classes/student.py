from random import randrange


class Student:
    def __init__(self, firstName: str, lastName: str, group: str, gpa: int):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.gpa = gpa

    def getScholarship(self):
        if self.gpa == 5:
            scholarship = 100
        else:
            scholarship = 80
        return scholarship


class Aspirant(Student):
    # overwrites original method
    def getScholarship(self):
        if self.gpa == 5:
            scholarship = 200
        else:
            scholarship = 180
        return scholarship


# students and aspirant
learners = []

# random gpa
gpa_r = []

for student_id in range(5):

    # IDs for students
    learners.append(f'student_{student_id}')

    # random gpa (grade point average)
    gpa_r.append(randrange(1, 6))


for studs in learners:

    # even entries become aspirants
    if gpa_r[learners.index(studs)] % 2 == 0:
        studs = Aspirant('fn', 'ln', 'gr', gpa_r[learners.index(studs)])
        print(studs.getScholarship())

    # odd entries become students
    else:
        studs = Student('fn', 'ln', 'gr', gpa_r[learners.index(studs)])
        print(studs.getScholarship())
