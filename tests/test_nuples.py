import pytest
from typographeur import typographeur


@pytest.mark.parametrize("input,expected", [
    ('hello???', 'hello&#8239;???'),
    ('hello ???', 'hello&#8239;???'),
    ('hello ???', 'hello&#8239;???'),  # Fine insecable
    ('hello ??', 'hello&#8239;???'),
    ('hello ??????', 'hello&#8239;???'),
])
def test_triple_question(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ('hello!!!', 'hello&#8239;!!!'),
    ('hello !!!', 'hello&#8239;!!!'),
    ('hello !!!', 'hello&#8239;!!!'),  # Fine insecable
    ('hello !!', 'hello&#8239;!!!'),
    ('hello !!!!!', 'hello&#8239;!!!'),
])
def test_triple_exclamation(input, expected):
    output = typographeur(input)
    assert output == expected


# Let's agree on something: this kind of writings doesn't exist.
@pytest.mark.parametrize("input,expected", [
    ('hello;;;', 'hello&#8239;;;;'),
    ('hello ;;;', 'hello&#8239;;;;'),
    ('hello ;;;', 'hello&#8239;;;;'),  # Fine insecable
    ('hello ;;', 'hello&#8239;;;'),
    ('hello ;;;;;', 'hello&#8239;;;;;;'),
])
def test_triple_semicolon(input, expected):
    output = typographeur(input)
    assert output == expected
