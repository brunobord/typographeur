from os.path import join
from pprint import pformat

variants = ['classique', 'moderne', 'reforme1990', 'toutesvariantes']


header = '''"""
Ligature dictionary
"""
'''


class Word(object):
    def __init__(self, wordline):
        self._line = wordline  # for debugging
        if "/" in wordline:
            self.word, _, self.tags = wordline.partition('/')
        else:
            self.word = wordline.split()[0]
            self.tags = ""

    @property
    def has_plural(self):
        if not self.tags:
            return False
        if "is:inv" in self.tags:  # invariable
            return False
        if "po:v" in self.tags:  # verbe
            return False
        if "is:pl" in self.tags:  # déjà au pluriel
            return False
        if "is:sg" in self.tags:  # forme singulier / pluriel à part
            return False
        return True

    @property
    def plural_form(self):
        if self.has_plural:
            if self.tags[0] in ("S", "F", "W"):
                return "s"
            if self.tags[0] == "X":
                return "x"
            raise Exception((self.word, self.tags))


def read_variant(variant):
    with open(join("sources", f"fr-{variant}.dic"), 'r') as fd:
        for line in fd.readlines():
            if 'œ' in line or 'æ' in line:
                yield line


def generate_words_with_plural(variant, words):
    oe_words_source = filter(lambda x: variant in x, words)
    oe_words_source = map(Word, oe_words_source)
    for word in oe_words_source:
        yield word.word
        if word.has_plural:
            yield f'{word.word}{word.plural_form}'


def generate_variant(variant):
    words = read_variant(variant)
    words = map(lambda x: x.strip(), words)
    words = list(words)
    words = filter(lambda x: len(x) > 1, words)
    # There are about 200 words with ligatures, I think we can safely turn
    # this into a list
    words = list(words)
    oe_words = generate_words_with_plural('œ', words)
    ae_words = generate_words_with_plural('æ', words)
    return oe_words, ae_words


def clean_wordlist(wordlist):
    wordlist = tuple(sorted(set(wordlist)))
    wordlist = pformat(wordlist, indent=4)
    wordlist = wordlist.replace('(   ', '(\n    ')
    return wordlist


if __name__ == '__main__':
    fd = open(join('..', 'typographeur', 'ligatures.py'), 'w')
    fd.write(header)
    fd.write('\n\n')

    dictionaries = {}

    for variant in variants:
        oe_words, ae_words = generate_variant(variant)
        oe_words = clean_wordlist(oe_words)
        ae_words = clean_wordlist(ae_words)
        fd.write(f'OE_{variant.upper()} = {oe_words}')
        fd.write('\n\n')
        fd.write(f'AE_{variant.upper()} = {ae_words}')
        fd.write('\n\n')

    fd.write('ligature_dictionaries = {\n')
    for variant in variants:
        fd.write(f'    "{variant}": ')
        fd.write('{')
        fd.write(f'"œ": OE_{variant.upper()}, "æ": AE_{variant.upper()}')
        fd.write('},\n')
    fd.write('}\n')

    fd.close()
