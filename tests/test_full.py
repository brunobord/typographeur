from os.path import join, dirname

from typographeur import typographeur


def test_full():
    path = dirname(__file__)
    _input = open(join(path, 'examples/input.html')).read()
    expected = open(join(path, 'examples/expected.html')).read()
    output = typographeur(_input)
    assert output == expected
