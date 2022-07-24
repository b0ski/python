import pytest
from app.strings.wordcount import word_count


@pytest.mark.parametrize(
    'a,  answer',
    [
        ('Function gets dog, where words split with space', 8),
        ('Функція отриму', 2),
    ]
)
def test_wordcount(a, answer):
    assert answer == word_count(a)
