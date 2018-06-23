from os.path import join, dirname

from typographeur import typographeur

root = dirname(__file__)


def test_full():
    _input = open(join(root, 'examples/input.html')).read()
    expected = open(join(root, 'examples/expected.html')).read()
    output = typographeur(_input)
    assert output == expected


def test_markdown():
    _input = open(join(root, 'examples/input.md')).read()
    expected = open(join(root, 'examples/expected.md')).read()
    # Markdown output is ugly with HTML entities for insecable spaces.
    output = typographeur(_input, fix_nbsp=False)
    assert output == expected
