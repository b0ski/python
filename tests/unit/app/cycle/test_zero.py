import pytest
from app.cycle.zero import zero


@pytest.mark.parametrize(
    '*first,  answer',
    [
        (12, 6),
        (2, 2),
    ]
)
def test_zero(first, answer):
    assert answer == zero(first)