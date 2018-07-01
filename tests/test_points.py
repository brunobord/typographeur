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


@pytest.mark.parametrize("input,expected", [
    ("<h1>Titre</h1>", "<h1>Titre</h1>"),
    ("<h1>Titre.</h1>", "<h1>Titre</h1>"),
    ("<h2>Titre.</h2>", "<h2>Titre</h2>"),
    ("<h3>Titre.</h3>", "<h3>Titre</h3>"),
    ("<h4>Titre.</h4>", "<h4>Titre</h4>"),
    ("<h5>Titre.</h5>", "<h5>Titre</h5>"),
    ("<h6>Titre.</h6>", "<h6>Titre</h6>"),
])
def test_heading_points(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ("<title>Titre.</title>", "<title>Titre</title>"),
    ("<title>Titre.\n</title>", "<title>Titre</title>"),
    ("<title>Titre.\nAutre titre.</title>",
     "<title>Titre.\nAutre titre</title>"),
])
def test_title_points(input, expected):
    output = typographeur(input)
    assert output == expected
