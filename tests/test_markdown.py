from os.path import join, dirname

from typographeur import typographeur_markdown

root = dirname(__file__)


def test_full():
    _input = open(join(root, 'examples/input.md')).read()
    expected = open(join(root, 'examples/expected.md')).read()
    output = typographeur_markdown(_input)
    assert output == expected
