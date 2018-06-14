import pytest
from typographeur import typographeur
from .fixtures_factory import _build_fixture_insecable


@pytest.mark.parametrize("input,expected", _build_fixture_insecable(':'))
def test_colon(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", _build_fixture_insecable('!'))
def test_exclamation(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", _build_fixture_insecable('?'))
def test_question(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", _build_fixture_insecable(';'))
def test_semicolon(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    (
        "<p>Exemple : <em>Salut ! ça va ?</em></p>\nIci ; j'aime",
        "<p>Exemple&nbsp;: <em>Salut&nbsp;! ça va&nbsp;?</em></p>"
        "\nIci&nbsp;; j'aime"
    ),
])
def test_insecable(input, expected):
    output = typographeur(input)
    assert output == expected
