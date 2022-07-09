import pytest
from app.conditional_operator.rook import rook


@pytest.mark.parametrize(
    'r1, r2, t1, t2, answer',
    [
        ('f', 7, 'f', 2, 'Yes'),
        ('a', 4, 'c', 1, 'No')
    ]
)
def test_rook(r1, r2, t1, t2, answer):
    assert answer == rook(r1, r2, t1, t2)



