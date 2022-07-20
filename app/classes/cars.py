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