import pytest
from app.lists.reverse import reverse


@pytest.mark.parametrize(
    'a,  answer',
    [
        ([1, 666662, 43, 2345, 3245, 4232], [4232, 3245, 2345, 43, 666662, 1]),
    ]
)
def test_even_max_num(a, answer):
    assert answer == reverse(a)
