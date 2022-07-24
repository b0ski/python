import pytest
from app.conditional_operator.greater import greater


@pytest.mark.parametrize(
    'first, second, answer',
    [
        (1, 3, 3),
        (10, 40, 40),
        (-10, 2, 2),
    ]
)
def test_greater(first, second, answer):
    assert answer == greater(first, second)
