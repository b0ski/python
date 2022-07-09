import pytest
from app.cycle.sum import sum


@pytest.mark.parametrize(
    '*first,  answer',
    [
        (12, 6),
        (2, 2),
    ]
)
def test_sum(first, answer):
    assert answer == sum(first)
