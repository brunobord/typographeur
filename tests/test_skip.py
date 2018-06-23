import pytest
from typographeur import typographeur, TAGS_TO_SKIP


# Generate fixtures
skip_fixture_simple = [
    [f'<{tag}>hello!</{tag}>'] * 2 for tag in TAGS_TO_SKIP
]


@pytest.mark.parametrize("input,expected", skip_fixture_simple)
def test_skip_simple(input, expected):
    output = typographeur(input)
    assert output == expected


@pytest.mark.parametrize("input,expected", [
    ('<code />hello .', '<code />hello.'),
    ('<code/>hello .', '<code/>hello.'),
    ('<code attr="meuh" />hello .', '<code attr="meuh" />hello.'),
    ('<pre />hello .', '<pre />hello.'),
    ('<pre/>hello .', '<pre/>hello.'),
])
def test_auto_closed(input, expected):
    output = typographeur(input)
    assert output == expected
