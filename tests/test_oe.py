import pytest
from typographeur import typographeur


@pytest.mark.parametrize('input,expected', [
    ("un truc dans l'oeil", "un truc dans l’œil"),
    ("un truc dans l'oeil", "un truc dans l’œil"),
    ("un truc dans l'oeilgrrr", "un truc dans l’oeilgrrr"),  # unknown word
    ("oeil-de-truc", "œil-de-truc"),  # compound word at the beginning
    ("un oeil, des yeux", "un œil, des yeux"),
])
def test_oe(input, expected):
    output = typographeur(input)
    assert output == expected
