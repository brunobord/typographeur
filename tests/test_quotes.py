import pytest
from typographeur import typographeur


@pytest.mark.parametrize("input,expected", [
    ('"hello"', '«&nbsp;hello&nbsp;»'),
    ('" hello   "', '«&nbsp;hello&nbsp;»'),
    ('"   hello    "', '«&nbsp;hello&nbsp;»'),  # multiple insecable spaces
    (
        '"hello" je vais "bien"',
        '«&nbsp;hello&nbsp;» je vais «&nbsp;bien&nbsp;»'
    ),
])
def test_parenthesis(input, expected):
    output = typographeur(input)
    assert output == expected
