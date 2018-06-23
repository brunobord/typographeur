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
def test_quotes(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ('<p class="something">hello</p>', '<p class="something">hello</p>'),
])
def test_dont_convert_html_attributes(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ("<p>l'éléphant</p>", "<p>l’éléphant</p>"),
    ("<p>l' éléphant</p>", "<p>l’éléphant</p>"),
    ("<p>j'aime l'éléphant</p>", "<p>j’aime l’éléphant</p>"),
    ("<p>l'<em>éléphant</em></p>", "<p>l’<em>éléphant</em></p>"),
    ("<p>L'éléphant</p>", "<p>L’éléphant</p>"),
    ("<p>L'<em>éléphant</em></p>", "<p>L’<em>éléphant</em></p>"),
    ("<p>Ç'a n'existe pas</p>", "<p>Ç’a n’existe pas</p>"),
])
def test_apostrophe(input, expected):
    output = typographeur(input)
    assert output == expected
