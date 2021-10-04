WRONG_NUMBER_OF_SEPARATORS = ('Wrong number of separators.' 
                              'Should be 2, found {}.')
WRONG_PREFIX = 'Separator not found in prefix.'
ORIGINAL_WORD_NOT_FOUND = 'None of the original words matches the word {}'


class WrongNumOfSeparatorsError(Exception):
    """Exception raised when there aren't 2 separators.

    Attributes:
        num_of_separators -- number of found separators
        message -- explanation of the error
    """

    def __init__(
            self, num_of_separators: int,
            message: str = WRONG_NUMBER_OF_SEPARATORS,
    ) -> None:
        self.num_of_separators = num_of_separators
        self.message = message.format(str(self.num_of_separators))
        super().__init__(self.message)


class NoSeparatorAsPrefixError(Exception):
    """Exception raised when there isn't separator as a prefix.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = WRONG_PREFIX) -> None:
        self.message = message
        super().__init__(self.message)


class OriginalWordNotFoundError(Exception):
    """Exception raised when none of original words matches encoded word.

    Attributes:
        encoded_word -- number of found separators
        message -- explanation of the error
    """

    def __init__(
            self, encoded_word: str, message: str = ORIGINAL_WORD_NOT_FOUND,
    ) -> None:
        self.encoded_word = encoded_word
        self.message = message.format(self.encoded_word)
        super().__init__(self.message)
