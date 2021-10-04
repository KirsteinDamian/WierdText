from commons import TOKENIZER_RE, SEPARATOR, is_shuffleable
from exceptions import NoSeparatorAsPrefixError, OriginalWordNotFoundError,\
    WrongNumOfSeparatorsError


def validate_sentence(sentence: str) -> None:
    if (num_of_separators := sentence.count(SEPARATOR)) != 2:
        raise WrongNumOfSeparatorsError(num_of_separators)
    if not sentence.startswith(SEPARATOR):
        raise NoSeparatorAsPrefixError()


def _does_words_matches(original_word: str, word: str) -> bool:
    return(
        len(original_word) == len(word) and
        original_word[0] == word[0] and
        original_word[-1] == word[-1] and
        sorted(original_word[1:-1]) == sorted(word[1:-1])
    )


def decode(sentence: str) -> str:
    decoded_sentence = ''
    validate_sentence(sentence)
    encoded_sentence, original_words_str = sentence[
                                           len(SEPARATOR):].split(SEPARATOR)
    encoded_words = TOKENIZER_RE.split(encoded_sentence)
    original_words = original_words_str.split()
    for word in encoded_words:
        if is_shuffleable(word):
            matched_words = [
                original_word
                for original_word in original_words
                if _does_words_matches(original_word, word)
            ]
            if not matched_words:
                raise OriginalWordNotFoundError(word)
            decoded_sentence += matched_words[0]
        else:
            decoded_sentence += word
    return decoded_sentence
