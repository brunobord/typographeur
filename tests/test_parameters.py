import pytest
from typographeur import typographeur


def test_parenthesis():
    input = '( hello )'
    output = typographeur(input, fix_parenthesis=False)
    assert output == input


def test_colon():
    input = 'hello:'
    output = typographeur(input, fix_colon=False)
    assert output == input


def test_exclamation():
    input = 'hello!'
    output = typographeur(input, fix_exclamation=False)
    assert output == input


def test_interrogation():
    input = 'hello?'
    output = typographeur(input, fix_interrogation=False)
    assert output == input


def test_semicolon():
    input = 'hello;'
    output = typographeur(input, fix_semicolon=False)
    assert output == input


def test_ellipsis():
    input = 'hello...'
    output = typographeur(input, fix_ellipsis=False)
    assert output == input


def test_point_space():
    input = 'hello …'
    output = typographeur(input, fix_point_space=False)
    assert output == input
    input = 'hello . world'
    output = typographeur(input, fix_point_space=False)
    assert output == input


def test_comma_space():
    input = 'hello ,'
    output = typographeur(input, fix_comma_space=False)
    assert output == input


def test_double_quotes():
    input = '"hello"'
    output = typographeur(input, fix_double_quote=False)
    assert output == input


def test_apostrophes():
    input = "l'éléphant"
    output = typographeur(input, fix_apostrophes=False)
    assert output == input


@pytest.mark.parametrize("input,expected", [
    ('hello:', 'hello :'),
    ('hello :', 'hello :'),  # normal space
    ('hello :', 'hello :'),  # insecable space
])
def test_nbsp(input, expected):
    output = typographeur(input, fix_nbsp=False)
    # spaces are replaced by insecable spaces,
    # insecable spaces are not replaced by `&nbsp;`
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ('hello??', 'hello&#8239;??'),
    ('hello!!', 'hello&#8239;!!'),
    ('hello ??', 'hello&#8239;??'),
    ('hello !!', 'hello&#8239;!!'),
])
def test_nuples(input, expected):
    output = typographeur(input, fix_nuples=False)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ("<h1>Titre</h1>", "<h1>Titre</h1>"),
    ("<h1>Titre.</h1>", "<h1>Titre.</h1>"),
    ("<h2>Titre.</h2>", "<h2>Titre.</h2>"),
    ("<h3>Titre.</h3>", "<h3>Titre.</h3>"),
    ("<h4>Titre.</h4>", "<h4>Titre.</h4>"),
    ("<h5>Titre.</h5>", "<h5>Titre.</h5>"),
    ("<h6>Titre.</h6>", "<h6>Titre.</h6>"),
    ("<title>Titre.</title>", "<title>Titre.</title>"),
])
def test_title_points(input, expected):
    output = typographeur(input, fix_title_points=False)
    assert output == expected


@pytest.mark.parametrize("input", [
    "un oeil, des yeux",
    "un œil, des yeux",
])
def test_oe(input):
    output = typographeur(input, fix_oe=False)
    assert output == input


@pytest.mark.parametrize("input", [
    "une novae, des supernovae",
    "un novæ, des supernovæ",
])
def test_ae(input):
    output = typographeur(input, fix_ae=False)
    assert output == input


def test_ligature_variant():
    with pytest.raises(ValueError):
        typographeur("", ligature_variant="unknown")

    with pytest.raises(ValueError):
        typographeur("", fix_ae=False, ligature_variant="unknown")

    with pytest.raises(ValueError):
        typographeur("", fix_oe=False, ligature_variant="unknown")

    try:
        typographeur("", fix_ae=False, fix_oe=False,
                     ligature_variant="unknown")
    except ValueError:
        pytest.fail("Should not raise any exception")


def test_ligature_classique():
    # the word "angstrœm" is not in 'classique', but is in 'reforme1990'
    result = typographeur("angstroem", ligature_variant="classique")
    assert result == "angstroem"

    result = typographeur("angstroem", ligature_variant="reforme1990")
    assert result == "angstrœm"
