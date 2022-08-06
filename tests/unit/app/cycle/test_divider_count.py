import pytest
from app.cycle.divider_count import divider_counter


@pytest.mark.parametrize(
    'first,  answer',
    [
        (12, 6),
        (2, 2),
    ]
)
def test_divider_count(first, answer):
    assert answer == divider_counter(first)
