from collections import namedtuple
from enum import Enum, auto


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
    WHITESPACE = auto()


class FredsonTokenError(Exception):
    pass


Token = namedtuple('Token', ['token_type', 'lexeme'])


class CharacterQueue:
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
        n = n if n < len(self) else len(self)
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
        raise FredsonTokenError(error_message)


class FredsonParseError(Exception):
    pass

