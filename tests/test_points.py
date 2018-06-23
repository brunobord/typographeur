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


@pytest.mark.parametrize("input,expected", [
    ("Je cite [..] mais pas entièrement.",
     "Je cite [..] mais pas entièrement."),
    ("Je cite [...] mais pas entièrement.",
     "Je cite [..] mais pas entièrement."),
    ("Je cite […] mais pas entièrement.",
     "Je cite [..] mais pas entièrement."),
])
def test_dual_points(input, expected):
    output = typographeur(input)
    assert output == expected
