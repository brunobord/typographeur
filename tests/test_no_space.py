import pytest
from typographeur import typographeur


@pytest.mark.parametrize("input,expected", [
    ('(hello)', '(hello)'),
    ('( hello )', '(hello)'),
    ('(   hello    )', '(hello)'),
    ('(   hello    )', '(hello)'),  # insecable here
])
def test_parenthesis(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ('hello.', 'hello.'),
    ('hello .', 'hello.'),
    ('hello  .', 'hello.'),   # normal spaces
    ('hello .', 'hello.'),  # insecable here
    ('hello  .', 'hello.'),  # double insecable here
    ('hello   .', 'hello.'),  # insecable + normal here
])
def test_point(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ('hello…', 'hello…'),
    ('hello …', 'hello…'),
    ('hello  …', 'hello…'),   # normal spaces
    ('hello …', 'hello…'),  # insecable here
    ('hello  …', 'hello…'),  # double insecable here
    ('hello   …', 'hello…'),  # insecable + normal here
])
def test_triple_point(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ('hello,', 'hello,'),
    ('hello ,', 'hello,'),
    ('hello  ,', 'hello,'),   # normal spaces
    ('hello ,', 'hello,'),  # insecable here
    ('hello  ,', 'hello,'),  # double insecable here
    ('hello   ,', 'hello,'),  # insecable + normal here
])
def test_comma(input, expected):
    output = typographeur(input)
    assert output == expected
