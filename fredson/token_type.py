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
