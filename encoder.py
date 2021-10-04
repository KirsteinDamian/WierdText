import random

from commons import TOKENIZER_RE, SEPARATOR, is_shuffleable


def shuffle_word(word: str) -> str:
    """
    Shuffle characters of the word.
    First and the last characters don't change.
    """
    middle_characters = list(word[1:-1])
    random.shuffle(middle_characters)
    return word[0] + ''.join(middle_characters) + word[-1]


def encode(sentence: str) -> str:
    """
    Encode a sentence in Unicode.
    Note: shuffle_word may return the same value as argument, so we need
          to ensure if shuffled word has changed
    :return
    '\n—weird—\n'
    '{encoded sentence}'
    '\n—weird—\n'
    '{sorted list of original words}'
    """
    encoded_sentence = SEPARATOR
    sorted_words = []
    words = TOKENIZER_RE.split(sentence)
    for word in words:
        if is_shuffleable(word):
            sorted_words.append(word)
            while True:
                if word != (shuffled_word := shuffle_word(word)):
                    break
            encoded_sentence += shuffled_word
        else:
            encoded_sentence += word
    sorted_words.sort()
    return encoded_sentence + SEPARATOR + ' '.join(sorted_words)
