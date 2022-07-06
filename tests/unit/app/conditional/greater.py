import pytest
from app.conditional.greater import greater


@pytest.mark.parametrize(
    'first, second, answer',
    [
        (1, 2, 2),
        (-1, 0, 0),
        (0, 2, 2),
    ]
)
def test_conditional(first, second, answer):
    assert answer == greater(first, second)


def test_conditional_exception():
    with pytest.raises(TypeError):
        greater('asd', 2)
    with pytest.raises(TypeError):
        greater(10.2, 2)
