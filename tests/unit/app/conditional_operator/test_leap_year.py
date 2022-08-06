import pytest
from app.conditional_operator.leap_year import leap_year


@pytest.mark.parametrize(
    'first, answer',
    [
        (2000, 'Yes'),
        (2001, 'No'),
        (2004, 'Yes'),
    ]
)
def test_leap_year(first, answer):
    assert answer == leap_year(first)




