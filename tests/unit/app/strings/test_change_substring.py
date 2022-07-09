import pytest
from app.strings.change_substring import change_substring


@pytest.mark.parametrize(
    'a,  answer',
    [
        ('01 2311 6119', '0one 23oneone 6oneone9'),
    ]
)
def test_change_substring(a, answer):
    assert answer == change_substring(a)




