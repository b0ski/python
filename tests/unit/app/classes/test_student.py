import pytest
from app.classes.student import Student, Aspirant


@pytest.mark.parametrize(
    'firstName, lastName, group, gpa, ans',
    [
        ('Petro', 'Petrenko', 'asd-60', 4, 80
         ),
    ]
)
def test_getScholarship(firstName: str, lastName: str, group: str, gpa: int, ans):
    student = Student(firstName, lastName, group, gpa)
    assert student.getScholarship() == ans








