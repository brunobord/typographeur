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
