import pytest

from commons import SEPARATOR, is_shuffleable
from decoder import decode
from encoder import encode
from exceptions import WrongNumOfSeparatorsError, WRONG_NUMBER_OF_SEPARATORS, \
    NoSeparatorAsPrefixError, WRONG_PREFIX, OriginalWordNotFoundError, \
    ORIGINAL_WORD_NOT_FOUND


def test_encode():
    original_text = 'Short text'
    encoded = encode(original_text)
    assert encoded.count(SEPARATOR) == 2
    assert original_text == encoded[-len(original_text):]


def test_decode():
    original_text = 'Short text'
    encoded_text = '\n—weird—\nSrhot txet\n—weird—\nShort text'
    assert original_text == decode(encoded_text)


@pytest.mark.parametrize('encoded_text, separators_count', [
    ('Srhot txet\n—weird—\nShort text', 1),
    ('\n—weird—\nSrhot txet\n—weird—\nShort text\n—weird—\n', 3),
])
def test_decode_raise_wrong_num_of_separators_error(
        encoded_text, separators_count,
):
    with pytest.raises(WrongNumOfSeparatorsError) as error:
        decode(encoded_text)
    assert WRONG_NUMBER_OF_SEPARATORS.format(
        separators_count) == error.value.message


def test_decode_raise_no_separator_as_prefix_error():
    with pytest.raises(NoSeparatorAsPrefixError) as error:
        decode('Srhot txet\n—weird—\nShort text\n—weird—\n')
    assert WRONG_PREFIX == error.value.message


def test_decode_raise_original_word_not_found_error():
    with pytest.raises(OriginalWordNotFoundError) as error:
        decode('\n—weird—\nSrhot txet\n—weird—\nShot Shhort Thort Shotd text')
    assert ORIGINAL_WORD_NOT_FOUND.format('Srhot') == error.value.message


@pytest.mark.parametrize('word, shuffleable', [
    ('', False),
    ('A', False),
    ('FCB', False),
    ('%$!', False),
    ('Verylongword', True),
    ('Leeeeeel', False),
])
def test_is_shuffleable(word, shuffleable):
    assert shuffleable == is_shuffleable(word)


@pytest.mark.parametrize('original_text', [
    '',
    'Py',
    'Test',
    'Th is is sh ort',
    'This include num83rs',
    'Spec!al charact3r$',  # pass, but encoding is not correct
    '^%&^#%$&$ $#*&#',
    ('This is a long looong test sentence,\n'
     'with some big (biiiiig) words!'),
])
def test_integration(original_text):
    encoded = encode(original_text)
    decoded = decode(encoded)
    assert original_text == decoded
