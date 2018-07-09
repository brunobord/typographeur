from os.path import join, dirname

from typographeur import typographeur

root = dirname(__file__)


def test_full():
    _input = open(join(root, 'examples/input.html')).read()
    expected = open(join(root, 'examples/expected.html')).read()
    output = typographeur(_input)
    assert output == expected
