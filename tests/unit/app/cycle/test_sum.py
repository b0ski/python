import pytest
from app.cycle.sum import sum


@pytest.mark.parametrize(
    'first,  answer',
    [
        ([1, 2], 3),
        ([5, 2], 7),
    ]
)
def test_sum(first, answer):
    assert answer == sum(*first)
