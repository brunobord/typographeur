import pytest
from typographeur import typographeur


@pytest.mark.parametrize("input,expected", [
    ('hello...', 'hello…'),
    ('hello…', 'hello…'),
    ('hello..', 'hello…'),
    ('hello....', 'hello…'),
    ('hello.........', 'hello…'),
])
def test_points(input, expected):
    output = typographeur(input)
    assert output == expected
