import pytest
from app.lists.unique import unique


@pytest.mark.parametrize(
    'a,  answer',
    [
        ([1, 22, 22, 11, 11, 11, 22, 333], [1, 333]),
    ]
)
def test_unique(a, answer):
    assert answer == unique(a)

