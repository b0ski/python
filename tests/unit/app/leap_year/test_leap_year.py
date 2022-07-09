import pytest
from app.math.math import plus


@pytest.mark.parametrize(
    'first, second, answer',
    [
        (1, 2, 3),
        (10, 30, 40),
        (-10, 2, -8),
    ]
)
def test_plus(first: int, second: int, answer: int):
    assert answer == plus(first, second)


def test_plus_exception():
    with pytest.raises(TypeError):
        plus(10, 's')
    with pytest.raises(TypeError):
        plus('asd', 2)
    with pytest.raises(TypeError):
        plus(10.2, 2)
