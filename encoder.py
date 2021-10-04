import random

from commons import TOKENIZER_RE, SEPARATOR, is_shuffleable


def shuffle_word(word: str) -> str:
    middle_characters = list(word[1:-1])
    random.shuffle(middle_characters)
    return word[0] + ''.join(middle_characters) + word[-1]


def encode(sentence: str) -> str:
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
