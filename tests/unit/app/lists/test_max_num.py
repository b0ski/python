import pytest
from app.lists.max_num import max_num


@pytest.mark.parametrize(
    'a,  answer',
    [
        ((1, 666662, 43, 2345, 3245, 4232), (666662, 1)),
    ]
)
def test_even_max_num(a, answer):
    assert answer == max_num(a)



