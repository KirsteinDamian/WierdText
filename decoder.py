from commons import TOKENIZER_RE, SEPARATOR, is_shuffleable
from exceptions import NoSeparatorAsPrefixError, OriginalWordNotFoundError,\
    WrongNumOfSeparatorsError


def validate_sentence(sentence: str) -> None:
    if (num_of_separators := sentence.count(SEPARATOR)) != 2:
        raise WrongNumOfSeparatorsError(num_of_separators)
    if not sentence.startswith(SEPARATOR):
        raise NoSeparatorAsPrefixError()


def _does_words_matches(original_word: str, encoded_word: str) -> bool:
    """
    Check if original word matches encoded word.
    :param original_word: Word saved in list as original, not encoded.
    :param encoded_word: Word encoded by encoder.encode method.
    :return: True if encoded word has been made of original word,
             otherwise false.
    """
    return(
        len(original_word) == len(encoded_word) and
        original_word[0] == encoded_word[0] and
        original_word[-1] == encoded_word[-1] and
        sorted(original_word[1:-1]) == sorted(encoded_word[1:-1])
    )


def decode(sentence: str) -> str:
    """
    Decode sentence encoded with encoder.encode method.
    Note: not every sentence can be decoded correctly- example:
          'flot flat' -both words have 'f' as a prefix, 't' as a suffix and
          the same length. List of original words is sorted, so decode method
          will always choose the first original word.
    :param sentence: encoded string
    :return: decoded sentence
    """
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
