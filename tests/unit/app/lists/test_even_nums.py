import pytest
from app.lists.even_nums import even_nums


@pytest.mark.parametrize(
    'a,  answer',
    [
        ((1, 2, 43, 2345, 1245, 32), [2, 32]),
    ]
)
def test_even_even_nums(a, answer):
    assert answer == even_nums(a)

