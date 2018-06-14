
fixtures_insecable = [
    ("<p>exemple{mark}</p>", "<p>exemple&nbsp;{mark}</p>"),
    ("<p>exemple {mark}</p>", "<p>exemple&nbsp;{mark}</p>"),
    # insecable space below
    ("<p>exemple {mark}</p>", "<p>exemple&nbsp;{mark}</p>"),
    ("<p>exemple    {mark}</p>", "<p>exemple&nbsp;{mark}</p>"),
    ("<p>exemple    {mark} hello</p>", "<p>exemple&nbsp;{mark} hello</p>"),
    (
        "<p>exemple{mark} hello {mark} here</p>",
        "<p>exemple&nbsp;{mark} hello&nbsp;{mark} here</p>"),
]


def _build_fixture_insecable(mark):
    for _input, expected in fixtures_insecable:
        yield (_input.format(mark=mark), expected.format(mark=mark))
