import pytest
from typographeur import correcteur
from .fixtures_factory import _build_fixture_insecable


@pytest.mark.parametrize("input,expected", _build_fixture_insecable(':'))
def test_colon(input, expected):
    output = correcteur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", _build_fixture_insecable('!'))
def test_exclamation(input, expected):
    output = correcteur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", _build_fixture_insecable('?'))
def test_question(input, expected):
    output = correcteur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    (
        "<p>Exemple : <em>Salut ! ça va ?</em></p>",
        "<p>Exemple&nbsp;: <em>Salut&nbsp;! ça va&nbsp;?</em></p>"
    ),
])
def test_insecable(input, expected):
    output = correcteur(input)
    assert output == expected
