import pytest
from app.conditional_operator.knight import knight


@pytest.mark.parametrize(
    'first, second, third, fourth, answer',
    [
        ('d', 5, 'e', 3, 'Yes'),
        ('a', 4, 'v', 1, 'No'),
    ]
)
def test_knight(first, second, third, fourth, answer):
    assert answer == knight(first, second, third, fourth)


