"""
Typographeur, pour faire respecter les règles de typographie à la française.
"""
import re


INSECABLE_MARKS = (':', '!', '\?', ';')


def _tokenize(text):
    """
    Reference to an array of the tokens comprising the input string. Each token
    is either a tag (possibly with nested, tags contained therein, such as
    ``<a href="<MTFoo>">``, or a run of text between tags. Each element of the
    array is a two-element array; the first is either 'tag' or 'text'; the
    second is the actual value.
    Based on the _tokenize() subroutine from `Brad Choate's MTRegex plugin`__.
    __ http://www.bradchoate.com/past/mtregex.php
    """

    tokens = []

    tag_soup = re.compile(r'([^<]*)(<!--.*?--\s*>|<[^>]*>)', re.S)

    token_match = tag_soup.match(text)

    previous_end = 0
    while token_match:
        if token_match.group(1):
            tokens.append(['text', token_match.group(1)])

        # if -- in text part of comment, then it's not a comment, therefore it
        # should be converted.
        #
        # In HTML4 [1]:
        #   [...] Authors should avoid putting two or more adjacent hyphens
        #   inside comments.
        #
        # In HTML5 [2]:
        #   [...] the comment may have text, with the additional restriction
        #   that the text must not [...], nor contain two consecutive U+002D
        #   HYPHEN-MINUS characters (--)
        #
        # [1]: http://www.w3.org/TR/REC-html40/intro/sgmltut.html#h-3.2.4
        # [2]: http://www.w3.org/TR/html5/syntax.html#comments
        tag = token_match.group(2)
        type_ = 'tag'
        if tag.startswith('<!--'):
            # remove --[white space]> from the end of tag
            if '--' in tag[4:].rstrip('>').rstrip().rstrip('-'):
                type_ = 'text'
        tokens.append([type_, tag])

        previous_end = token_match.end()
        token_match = tag_soup.match(text, token_match.end())

    if previous_end < len(text):
        tokens.append(['text', text[previous_end:]])

    return tokens


def correcteur(text):
    tokens = _tokenize(text)
    print(tokens)
    result = []
    for token_type, token in tokens:
        if token_type == 'tag':
            result.append(token)
        else:
            for insecable_mark in INSECABLE_MARKS:
                mark = insecable_mark[-1]
                pattern = fr'((\s*?){insecable_mark})'
                token = re.sub(pattern, f' {mark}', token)
            result.append(token)

    result = "".join(result)
    result = result.replace(' ', '&nbsp;')
    return result
