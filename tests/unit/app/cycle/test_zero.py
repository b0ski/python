import pytest
from app.cycle.zero import zero


@pytest.mark.parametrize(
    'first,  answer',
    [
        ([1, 1, 0], 'Yes'),
    ]
)
def test_zero(first, answer):
    assert answer == zero(*first)