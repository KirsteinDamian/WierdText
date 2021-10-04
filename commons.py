import re

SEPARATOR = '\n—weird—\n'
TOKENIZER_RE = re.compile(r'(\w+)', re.U)


def is_shuffleable(word: str) -> bool:
    return (
            bool(TOKENIZER_RE.match(word)) and
            len(word) > 3 and
            len(set(word[1:-1])) > 1
    )
