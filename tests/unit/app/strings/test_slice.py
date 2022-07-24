import pytest
from app.strings.slice import slice


@pytest.mark.parametrize(
    '*first,  answer',
    [
        (12, 6),
        (2, 2),
    ]
)
def test_slice(first, answer):
    assert answer == slice(first)
