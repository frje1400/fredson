import re
import time

from collections import deque
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


class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

    def __str__(self):
        return f"{self.token_type}"

    def __repr__(self):
        return f"Token({self.token_type}, {self.lexeme})"


def tokenize(raw_json) -> deque[Token]:
    tokens = deque()
    characters = deque(raw_json)

    while len(characters) > 0:
        if characters[0] == '{':
            token = Token(TokenType.LEFT_BRACE, characters.popleft())
            tokens.append(token)
        elif characters[0] == '}':
            token = Token(TokenType.RIGHT_BRACE, characters.popleft())
            tokens.append(token)
        elif characters[0] == ':':
            token = Token(TokenType.SEMICOLON, characters.popleft())
            tokens.append(token)
        elif characters[0] == '[':
            token = Token(TokenType.LEFT_BRACKET, characters.popleft())
            tokens.append(token)
        elif characters[0] == ']':
            token = Token(TokenType.RIGHT_BRACKET, characters.popleft())
            tokens.append(token)
        elif characters[0] == ',':
            token = Token(TokenType.COMMA, characters.popleft())
            tokens.append(token)
        elif characters[0] == '"':
            token = tokenize_string(characters)
            tokens.append(token)
        elif re.match(r'\s', characters[0]):
            characters.popleft()
        elif re.match(r'[0-9]', characters[0]):
            token = tokenize_digits(characters)
            tokens.append(token)
        elif characters[0] == '.':
            token = Token(TokenType.DOT, characters.popleft())
            tokens.append(token)
        elif characters[0] == 'e' or characters[0] == 'E':
            token = Token(TokenType.EXPONENT, characters.popleft())
            tokens.append(token)
        elif characters[0] == '-':
            token = Token(TokenType.MINUS, characters.popleft())
            tokens.append(token)
        elif characters[0] == '+':
            token = Token(TokenType.PLUS, characters.popleft())
            tokens.append(token)
        elif re.match(r'[a-zA-Z]', characters[0]):
            token = tokenize_word(characters)
            tokens.append(token)
        else:
            raise Exception(f"invalid char: {characters[0]}")
    return tokens


def tokenize_word(characters):
    word = ""
    while len(characters) > 0 and re.match(r'[a-zA-Z]', characters[0]):
        word += characters.popleft()

    if word == "false":
        return Token(TokenType.FALSE, word)
    elif word == "true":
        return Token(TokenType.TRUE, word)
    elif word == "null":
        return Token(TokenType.NULL, word)
    else:
        raise Exception(f"tokenize_word: illegal word: {word}")


def tokenize_digits(characters: deque[str]) -> Token:
    digits = ""
    while len(characters) > 0 and re.match(r'[0-9]', characters[0]):
        digits += characters.popleft()

    # turn these into separate functions.
    if digits.startswith("0") and len(digits) > 1:
        # Returns e.g. 040529131889343 as a separate token type.
        return Token(TokenType.ZERO_DIGITS, digits)
    else:
        # Returns normal digit that starts with 1-9, or a single 0.
        return Token(TokenType.DIGITS, digits)


def tokenize_string(characters: deque[str]) -> Token:
    characters.popleft()  # pop opening quotation mark.
    string = ""
    while characters[0] != '"':
        string += characters.popleft()
    characters.popleft()  # pop closing quotation mark.
    return Token(TokenType.STRING, string)



