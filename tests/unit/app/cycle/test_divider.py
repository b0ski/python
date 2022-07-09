import pytest
from app.cycle.divider import divider


@pytest.mark.parametrize(
    'first,  answer',
    [
        (12, [1, 2, 3, 4, 6]),
    ]
)
def test_divider(first, answer):
    assert answer == divider(first)

