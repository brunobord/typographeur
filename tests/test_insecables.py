import pytest
from typographeur import typographeur


fixtures_insecable = [
    ("<p>exemple{mark}</p>", "<p>exemple{space}{mark}</p>"),
    ("<p>exemple {mark}</p>", "<p>exemple{space}{mark}</p>"),
    # insecable space below
    ("<p>exemple {mark}</p>", "<p>exemple{space}{mark}</p>"),
    ("<p>exemple    {mark}</p>", "<p>exemple{space}{mark}</p>"),
    ("<p>exemple    {mark} hello</p>", "<p>exemple{space}{mark} hello</p>"),
    (
        "<p>exemple{mark} hello {mark} here</p>",
        "<p>exemple{space}{mark} hello{space}{mark} here</p>"),
]


def _build_fixture_insecable(mark, space="&nbsp;"):
    for _input, expected in fixtures_insecable:
        yield (
            _input.format(mark=mark, space=space),
            expected.format(mark=mark, space=space)
        )


# colon -> espace insécable.
@pytest.mark.parametrize("input,expected", _build_fixture_insecable(':'))
def test_colon(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize(
    "input,expected", _build_fixture_insecable('!', '&#8239;'))
def test_exclamation(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize(
    "input,expected", _build_fixture_insecable('?', '&#8239;'))
def test_question(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize(
    "input,expected", _build_fixture_insecable(';', '&#8239;'))
def test_semicolon(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    (
        "<p>Exemple : <em>Salut ! ça va ?</em></p>\nIci ; j'aime",
        "<p>Exemple&nbsp;: <em>Salut&#8239;! ça va&#8239;?</em></p>"
        "\nIci&#8239;; j’aime"
    ),
])
def test_insecable(input, expected):
    output = typographeur(input)
    assert output == expected
