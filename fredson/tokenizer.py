import re

from character_queue import CharacterQueue
from collections import deque
from token_type import TokenType
from token_queue import TokenQueue, Token
from typing import Optional

SIMPLE_TOKENS = {
    '{': TokenType.LEFT_BRACE,
    '}': TokenType.RIGHT_BRACE,
    ':': TokenType.SEMICOLON,
    '.': TokenType.DOT,
    'e': TokenType.EXPONENT,
    'E': TokenType.EXPONENT,
    ',': TokenType.COMMA,
    '[': TokenType.LEFT_BRACKET,
    ']': TokenType.RIGHT_BRACKET,
}

KEYWORDS = {
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'null': TokenType.NULL
}

VALID_AFTER_BACKSLASH = {
    '\"': '\"',
    '\\': '\\',
    '/': '/',
    'b': '\b',
    'f': '\f',
    'n': '\n',
    'r': '\r',
    't': '\t'
}

WHITE_SPACE = {' ', '\n', '\r', '\t'}
DIGITS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
DIGITS_AND_DASH = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"}
LETTERS = re.compile(r'\w')
U_HEX_HEX_HEX_HEX = re.compile(r'u[a-fA-F0-9]{4}')


def tokenize(raw_json) -> TokenQueue:
    tokens = deque()
    characters = CharacterQueue(raw_json)

    while len(characters) > 0:
        first_char = characters[0]

        if first_char in SIMPLE_TOKENS:
            token = Token(SIMPLE_TOKENS[first_char], characters.next())
            tokens.append(token)
        elif first_char == '"':
            token = json_string(characters)
            tokens.append(token)
        elif first_char == '+':
            token = plus_sign(characters)
            tokens.append(token)
        elif first_char in WHITE_SPACE:
            tokens.append(Token(TokenType.WHITESPACE, characters.next()))
        elif first_char in DIGITS_AND_DASH:
            token = number(characters)
            tokens.append(token)
        elif LETTERS.match(first_char):
            token = keyword(characters)
            tokens.append(token)
        else:
            raise characters.error(f"Invalid char: {first_char}")

    return TokenQueue(tokens)


def plus_sign(characters: CharacterQueue) -> Token:
    plus = characters.next()
    if characters.peek() not in DIGITS:
        characters.error("Plus sign must be followed by [0-9]")
    return Token(TokenType.PLUS, plus)


def keyword(characters: CharacterQueue):
    word_characters = []
    while len(characters) > 0 and LETTERS.match(characters[0]):
        word_characters.append(characters.next())

    word = "".join(word_characters)

    if word in KEYWORDS:
        return Token(KEYWORDS[word], word)
    else:
        characters.error(f"Illegal keyword '{word}'")


def number(characters: CharacterQueue) -> Token:
    number_chars = [characters.next()]

    while len(characters) > 0 and characters[0] in DIGITS:
        number_chars.append(characters.next())

    num = "".join(number_chars)
    token = validate_number(num, characters)
    return token


def validate_number(num: str, characters: CharacterQueue) -> Token:
    if num.startswith("-") and len(num) == 1:
        characters.error("Found single minus sign without number.")
    elif num.startswith("-") and len(num) > 2 and num[1] == "0":
        characters.error("Found starting 0 in a number that starts with minus sign.")
    elif num.startswith("0") and len(num) > 1:
        return Token(TokenType.ZERO_DIGITS, num)
    else:
        return Token(TokenType.DIGITS, num)


def json_string(characters: CharacterQueue) -> Token:
    characters.ignore()  # pop opening quotation mark.
    string = []

    while (first_char := characters.next()) != '"':
        # Characters U+0000 (0) through U+001F (31) are control characters that must be
        # escaped. If we find such a character here, before we have seen a \, that is an
        # illegal character.
        if 0 <= ord(first_char) <= 31:
            raise characters.error(f"Illegal control character: {first_char}")
        elif first_char == "\\":
            next_char = handle_escape(characters)
            string.append(next_char)
        else:
            string.append(first_char)

    return Token(TokenType.STRING, "".join(string))


def handle_escape(characters: CharacterQueue) -> str:
    if characters.peek() in VALID_AFTER_BACKSLASH:
        return VALID_AFTER_BACKSLASH[characters.next()]
    elif characters.peek() == 'u':
        return starts_with_unicode(characters)
    else:
        raise characters.error(f"Illegal escape character: {characters[0]}")


def starts_with_unicode(characters: CharacterQueue) -> str:
    """If the characters start with u[a-fA-F0-9]{4} this method uses the four
    hex digits to return the corresponding character.

    Example: if the characters start with u0063, this method will return 'c'
    because chr(int('0063', 16)) -> 'c'.
    """
    if len(characters) < 5:
        characters.error("Not enough hex characters to parse unicode escape.")

    first_five = characters.take(5)
    code_point = first_five[1:]

    if re.match(U_HEX_HEX_HEX_HEX, first_five):
        if is_high_surrogate(code_point):
            # A high surrogate must be followed by a low surrogate. The high and low
            # surrogates are then combined to create a code point that is bigger than
            # 16 bits. This is looks strange but its purpose is to allow JSON to express
            # unicode using the unicode escape syntax (\u_hex_hex_hex_hex) while
            # simultaneously only using 16 bits per code point to stay compatible with
            # utf-16.
            return combine_high_low_surrogates(characters, code_point)

        return chr(int(code_point, 16))
    else:
        characters.error(f"Illegal unicode escape: {first_five}")


def combine_high_low_surrogates(characters: CharacterQueue, high_surrogate: str) -> str:
    low_surrogate_candidate = extract_low_surrogate(characters)

    if low_surrogate_candidate is None:
        # If we don't have a matching low surrogate the behavior of the builtin JSON module
        # is to return only the high surrogate.
        return chr(int(high_surrogate, 16))

    if is_low_surrogate(low_surrogate_candidate) is False:
        # If you have a high surrogate but then find that the expected low surrogate
        # isn't valid (i.e. in the range 0xDC00-0xDFFF you have a few different options:
        #
        #   1.  You could raise an error because the lack of the low surrogate
        #       makes it impossible to rebuild the code point using the high + low pair.
        #   2.  Keep the high surrogate and ignore the invalid low one.
        #   3.  Decode the invalid low surrogate as a normal \u_hex_hex_hex_hex code point.
        #
        # The third option is picked by Python's built in JSON parser and to stay as
        # compatible as possible with Python's normal behaviour we do that as well.
        return chr(int(high_surrogate, 16)) + chr(int(low_surrogate_candidate, 16))

    combined_code_point = high_low_surrogate_algorithm(high_surrogate, low_surrogate_candidate)
    return chr(combined_code_point)


def extract_low_surrogate(characters: CharacterQueue) -> Optional[str]:
    first_six = characters.peek(6)

    if re.match(r'\\u[a-fA-F0-9]{4}', first_six):
        backslash_u_code_point = characters.take(6)
        code_point = backslash_u_code_point[2:]
        return code_point
    else:
        return None


def is_high_surrogate(code_point: str) -> bool:
    start = 0xD800
    end_inclusive = 0xDBFF
    return start <= int(code_point, 16) <= end_inclusive


def is_low_surrogate(code_point: str) -> bool:
    start = 0xDC00
    end_inclusive = 0xDFFF
    return start <= int(code_point, 16) <= end_inclusive


def high_low_surrogate_algorithm(high_surrogate: str, low_surrogate: str) -> int:
    """Combines a high and low surrogate pair into a unicode code point."""
    # Algorithm for combining a high and low surrogate pair into a unicode code point:
    #   1. Take the high surrogate (0xD801) and subtract 0xD800, then multiply by 0x400,
    #   2. Take the low surrogate (0xDC37) and subtract 0xDC00.
    #   3. Add these two results together (0x0437), and finally add 0x10000 to get the final decoded UTF-32 code point.
    # source: https://en.wikipedia.org/wiki/UTF-16#U+D800_to_U+DFFF
    high = (int(high_surrogate, 16) - 0xD800) * 0x400
    low = int(low_surrogate, 16) - 0xDC00
    result = high + low + 0x10000
    return result
