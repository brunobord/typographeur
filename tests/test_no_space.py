import pytest
from typographeur import correcteur


@pytest.mark.parametrize("input,expected", [
    ('(hello)', '(hello)'),
    ('( hello )', '(hello)'),
    ('(   hello    )', '(hello)'),
    ('(   hello    )', '(hello)'),  # insecable here
])
def test_parenthesis(input, expected):
    output = correcteur(input)
    assert output == expected
