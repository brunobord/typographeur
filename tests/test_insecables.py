import pytest
from typographeur import typographeur


fixtures_insecable = [
    ("<p>exemple{mark}</p>", "<p>exemple&nbsp;{mark}</p>"),
    ("<p>exemple {mark}</p>", "<p>exemple&nbsp;{mark}</p>"),
    # insecable space below
    ("<p>exemple {mark}</p>", "<p>exemple&nbsp;{mark}</p>"),
    ("<p>exemple    {mark}</p>", "<p>exemple&nbsp;{mark}</p>"),
    ("<p>exemple    {mark} hello</p>", "<p>exemple&nbsp;{mark} hello</p>"),
    (
        "<p>exemple{mark} hello {mark} here</p>",
        "<p>exemple&nbsp;{mark} hello&nbsp;{mark} here</p>"),
]


def _build_fixture_insecable(mark):
    for _input, expected in fixtures_insecable:
        yield (_input.format(mark=mark), expected.format(mark=mark))


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
        "\nIci&nbsp;; j’aime"
    ),
])
def test_insecable(input, expected):
    output = typographeur(input)
    assert output == expected
