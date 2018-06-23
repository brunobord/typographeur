"""
Typographeur, pour faire respecter les règles de typographie à la française.
"""
from argparse import ArgumentParser, FileType
from collections import Counter
import re
import sys


__version__ = '0.2.0'
__all__ = ('typographeur',)

TAGS_TO_SKIP = ['pre', 'samp', 'code', 'tt', 'kbd', 'script', 'style', 'math']


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


def is_enter_skip(text):
    for tag in TAGS_TO_SKIP:
        if text.startswith(f'<{tag}'):
            return tag
    return False


def is_exit_skip(text):
    for tag in TAGS_TO_SKIP:
        if text.startswith(f'</{tag}'):
            return tag
    return False


def convert_quote(text):
    in_quote = False
    result = []
    for c in text:
        if c == '"':
            # starting quote
            if not in_quote:
                # Append guillemets + insecable space
                result.append('« ')
                in_quote = True
            else:
                # Append insecable space + closing guillemets
                result.append(' »')
                in_quote = False
        else:
            result.append(c)
    return ''.join(result)


def typographeur(text,
                 fix_parenthesis=True,
                 fix_colon=True, fix_exclamation=True,
                 fix_interrogation=True, fix_semicolon=True,
                 fix_ellipsis=True, fix_point_space=True,
                 fix_comma_space=True, fix_double_quote=True,
                 fix_apostrophes=True, fix_nbsp=True):
    """Apply french typography rules to the given text.

    :param text: The text to parse
    :param fix_parenthesis: apply the parenthesis rule.
    :param fix_colon: apply the rule for colons (:).
    :param fix_exclamation: apply the rule for exclamation points (!).
    :param fix_interrogation: apply the rule for interrogation points (?).
    :param fix_semicolon: apply the rule for semicolon (;).
    :param fix_ellipsis: apply the rule for ellipsis (... -> …).
    :param fix_point_space: remove spaces before points (. or …).
    :param fix_comma_space: remove spaces before commas (,).
    :param fix_double_quote: change double quotes into french guillemets («»).
    :param fix_apostrophes: change single quotes with typographic apostrophes.
    :param fix_nbsp: change insecable spaces into &nbsp; entities.
    :returns: The same text, with all rules applied.
    """
    tokens = _tokenize(text)
    result = []
    skip_counter = Counter()
    for token_type, token in tokens:
        if token_type == 'tag':
            # Check if it's a "enter" skip tag
            _is_enter_skip = is_enter_skip(token)
            _is_exit_skip = is_exit_skip(token)
            if _is_enter_skip:
                skip_counter[_is_enter_skip] += 1
            elif _is_exit_skip:
                skip_counter[_is_exit_skip] += 1
            result.append(token)
        else:
            if sum(skip_counter.values()):
                # We need to skip
                result.append(token)
                continue

            # Clear up &nbsp; entities into ' ' (insecable space)
            token = token.replace('&nbsp;', ' ')

            insecable_marks = set([':', '!', '\?', ';'])
            if not fix_colon:
                insecable_marks.remove(':')
            if not fix_exclamation:
                insecable_marks.remove('!')
            if not fix_interrogation:
                insecable_marks.remove('\?')
            if not fix_semicolon:
                insecable_marks.remove(';')

            for insecable_mark in insecable_marks:
                mark = insecable_mark[-1]
                pattern = fr'((\s*?){insecable_mark})'
                token = re.sub(pattern, f' {mark}', token)

            # Parenthesis
            if fix_parenthesis:
                token = re.sub(r'(\((\s+))', '(', token)
                token = re.sub(r'((\s+)\))', ')', token)

            # Points de suspension
            if fix_ellipsis:
                token = re.sub(r'(\.{2,})', '…', token)

            # No space before points
            if fix_point_space:
                token = re.sub(r'(\s+?)\.', '.', token)
                token = re.sub(r'(\s+?)…', '…', token)

            # No space before commas
            if fix_comma_space:
                token = re.sub(r'(\s+?),', ',', token)

            # Double quotes
            if fix_double_quote:
                token = convert_quote(token)
                token = re.sub(r'«(\s*)', '« ', token)
                token = re.sub(r'(\s*)»', ' »', token)

            # Apostrophes
            if fix_apostrophes:
                token = re.sub(r"(\w)'(\s*)", r'\1’', token)

            # Final token result
            result.append(token)

    result = "".join(result)
    # All changes have been made, we can convert insecable spaces back.
    if fix_nbsp:
        result = result.replace(' ', '&nbsp;')
    return result


def main():
    parser = ArgumentParser(
        "Typographeur, pour faire respecter "
        "les règles de typographie à la française."
    )
    parser.add_argument(
        '--version', action='version', version=__version__,
        help="Display current version"
    )

    parser.add_argument(
        '--skip-parenthesis', action='store_false',
        help="Don't apply parenthesis rule",
        default=True, dest='fix_parenthesis')
    parser.add_argument(
        '--skip-colon', action='store_false',
        help="Don't apply colon rule",
        default=True, dest='fix_colon')
    parser.add_argument(
        '--skip-exclamation', action='store_false',
        help="Don't apply exclamation point rule",
        default=True, dest='fix_exclamation')
    parser.add_argument(
        '--skip-interrogation', action='store_false',
        help="Don't apply interrogation point rule",
        default=True, dest='fix_interrogation')
    parser.add_argument(
        '--skip-semicolon', action='store_false',
        help="Don't apply semicolon rule",
        default=True, dest='fix_semicolon')
    parser.add_argument(
        '--skip-ellipsis', action='store_false',
        help="Don't apply ellipsis rule",
        default=True, dest='fix_ellipsis')
    parser.add_argument(
        '--skip-point-space', action='store_false',
        help="Don't apply the 'no space before points' rule",
        default=True, dest='fix_point_space')
    parser.add_argument(
        '--skip-comma-space', action='store_false',
        help="Don't apply the 'no space before commas' rule",
        default=True, dest='fix_comma_space')
    parser.add_argument(
        '--skip-double-quote', action='store_false',
        help="Don't transform double quotes into french guillemets",
        default=True, dest='fix_double_quote')
    parser.add_argument(
        '--skip-apostrophes', action='store_false',
        help="Don't transform single quotes into french apostrophes",
        default=True, dest='fix_apostrophes')
    parser.add_argument(
        '--skip-nbsp', action='store_false',
        help="Don't insecable spaces into HTML entities",
        default=True, dest='fix_nbsp')

    parser.add_argument(
        'files', metavar='FILE', type=FileType('r'),
        nargs='*', help='File(s) to be processed ')

    args = parser.parse_args()

    options = [arg for arg in dir(args) if arg.startswith('fix_')]
    options = {arg: getattr(args, arg) for arg in options}

    if args.files:
        for f in args.files:
            print(typographeur(f.read(), **options), end='')
    else:
        print(typographeur(sys.stdin.read(), **options), end='')
