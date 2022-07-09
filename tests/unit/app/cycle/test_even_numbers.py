import pytest
from app.cycle.even_numbers import even_numbers


@pytest.mark.parametrize(
    'first, second, answer',
    [
        (1, 10, [2, 4, 6, 8]),
        (1, 3, [2]),
    ]
)
def test_even_numbers(first, second, answer):
    assert answer == even_numbers(first, second)
