import re

from collections import deque, namedtuple
from enum import Enum, auto

import unicodedata


class TokenType(Enum):
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    STRING = auto()
    SEMICOLON = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COMMA = auto()
    DIGITS = auto()
    ZERO_DIGITS = auto()
    DOT = auto()
    EXPONENT = auto()
    MINUS = auto()
    PLUS = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()


Token = namedtuple('Token', ['token_type', 'lexeme'])

simple_tokens = {
    '{': TokenType.LEFT_BRACE,
    '}': TokenType.RIGHT_BRACE,
    ':': TokenType.SEMICOLON,
    '.': TokenType.DOT,
    '+': TokenType.PLUS,
    '-': TokenType.MINUS,
    'e': TokenType.EXPONENT,
    'E': TokenType.EXPONENT,
    ',': TokenType.COMMA,
    '[': TokenType.LEFT_BRACKET,
    ']': TokenType.RIGHT_BRACKET
}

keywords = {
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'null': TokenType.NULL
}

valid_after_backslash = {
    '\"': '\"',
    '/': '/',
    'b': '\b',
    'f': '\f',
    'n': '\n',
    'r': '\r',
    't': '\t'
}

white_space = re.compile(r'\s')
digits = re.compile(r'[0-9]')
letters = re.compile(r'\w')
u_hex_hex_hex_hex = re.compile(r'u[a-fA-F0-9]{4}')


class TokenizationError(Exception):
    pass


class Characters:
    def __init__(self, string: str):
        self.string = string
        self.size = len(string)
        self.current = 0

    def __len__(self) -> int:
        return self.size - self.current

    def __getitem__(self, index) -> str:
        return self.string[index + self.current]

    def take(self, n) -> str:
        s = self.string[self.current:self.current + n]
        self.current += n
        return s

    def peek(self, n=1):
        return self.string[self.current:self.current + n]

    def next(self) -> str:
        char = self.string[self.current]
        self.current += 1
        return char

    def ignore(self) -> None:
        self.current += 1

    def error(self, message) -> None:
        error_arrow = "\n" + " " * self.current + "^"
        error_message = f"\n{self.string}{error_arrow}\n{message}"
        raise TokenizationError(error_message)


def tokenize(raw_json) -> deque[Token]:
    tokens = deque()
    characters = Characters(raw_json)

    while len(characters) > 0:
        first_char = characters[0]

        if first_char in simple_tokens:
            token = Token(simple_tokens[first_char], characters.next())
            tokens.append(token)
        elif first_char == '"':
            token = json_string(characters)
            tokens.append(token)
        elif white_space.match(characters[0]):
            characters.next()
        elif digits.match(characters[0]):
            token = number(characters)
            tokens.append(token)
        elif letters.match(characters[0]):
            token = keyword(characters)
            tokens.append(token)
        else:
            raise Exception(f"invalid char: {first_char}")

    return tokens


def keyword(characters: Characters):
    word_characters = []
    while len(characters) > 0 and letters.match(characters[0]):
        word_characters.append(characters.next())

    word = "".join(word_characters)

    if word in keywords:
        return Token(keywords[word], word)
    else:
        characters.error('Illegal keyword.')


def number(characters: Characters) -> Token:
    number_characters = []
    while len(characters) > 0 and digits.match(characters[0]):
        number_characters.append(characters.next())

    num = "".join(number_characters)

    if num.startswith("0") and len(num) > 1:
        return Token(TokenType.ZERO_DIGITS, num)
    else:
        return Token(TokenType.DIGITS, num)


def json_string(characters: Characters) -> Token:
    characters.ignore()  # pop opening quotation mark.
    string = []

    while characters[0] != '"':
        first_char = characters.next()
        # According to the JSON spec you are not allowed to have "control characters"
        # in strings. An example of a control character is \n for new line. Because
        # JSON is unicode aware, it is not enough to look at the control characters
        # in the ASCII charset.
        #
        # The unicode standard defines certain categories for characters
        # where "control" is one such category. The unicode category for each character
        # is retrieved using Python's unicodedata module. The category is a one or two
        # character code that always starts with C for control characters.
        # https://www.unicode.org/reports/tr44/#GC_Values_Table

        # If this matching what it says in the rfc?
        # https://www.rfc-editor.org/rfc/rfc8259#section-7
        if unicodedata.category(first_char)[0] == 'C':
            raise Exception(f"Illegal control character found in string: {first_char}")

        if first_char == "\\":
            next_char = handle_escape(characters)
            string.append(next_char)
        else:
            string.append(first_char)

    characters.ignore()  # pop closing quotation mark.
    return Token(TokenType.STRING, "".join(string))


def handle_escape(characters: Characters) -> str:
    if characters[0] in valid_after_backslash:
        return valid_after_backslash[characters.next()]
    elif characters[0] == 'u':
        return starts_with_unicode(characters)
    else:
        raise characters.error("Illegal escape character.")


def starts_with_unicode(characters: Characters) -> str:
    """If the characters start with u[a-fA-F0-9]{4} this method uses the four
    hex digits to return the corresponding character.

    Example: if the characters start with u0063, this method will return 'c'
    because chr(int('0063', 16)) -> 'c'.
    """
    if len(characters) < 5:
        raise Exception("Not enough characters in starts_with_unicode.")

    first_five = characters.take(5)
    without_u = first_five[1:]

    if re.match(u_hex_hex_hex_hex, first_five):
        return chr(int(without_u, 16))
    else:
        characters.error("Illegal unicode escape.")


if __name__ == '__main__':
    pass
