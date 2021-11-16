import re
import unicodedata

from collections import deque
from definitions import TokenType, Token, CharacterQueue
from token_queue import TokenQueue


SIMPLE_TOKENS = {
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

KEYWORDS = {
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'null': TokenType.NULL
}

VALID_AFTER_BACKSLASH = {
    '\"': '\"',
    '/': '/',
    'b': '\b',
    'f': '\f',
    'n': '\n',
    'r': '\r',
    't': '\t'
}

WHITE_SPACE = re.compile(r'\s')
DIGITS = re.compile(r'[0-9]')
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
        elif WHITE_SPACE.match(characters[0]):
            tokens.append(Token(TokenType.WHITESPACE, characters.next()))
        elif DIGITS.match(characters[0]):
            token = number(characters)
            tokens.append(token)
        elif LETTERS.match(characters[0]):
            token = keyword(characters)
            tokens.append(token)
        else:
            raise characters.error(f"Invalid char: {first_char}")

    return TokenQueue(tokens)


def keyword(characters: CharacterQueue):
    word_characters = []
    while len(characters) > 0 and LETTERS.match(characters[0]):
        word_characters.append(characters.next())

    word = "".join(word_characters)

    if word in KEYWORDS:
        return Token(KEYWORDS[word], word)
    else:
        characters.error('Illegal keyword.')


def number(characters: CharacterQueue) -> Token:
    number_characters = []
    while len(characters) > 0 and DIGITS.match(characters[0]):
        number_characters.append(characters.next())

    num = "".join(number_characters)

    if num.startswith("0") and len(num) > 1:
        return Token(TokenType.ZERO_DIGITS, num)
    else:
        return Token(TokenType.DIGITS, num)


def json_string(characters: CharacterQueue) -> Token:
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
            raise characters.error(f"Illegal control character.")

        if first_char == "\\":
            next_char = handle_escape(characters)
            string.append(next_char)
        else:
            string.append(first_char)

    characters.ignore()  # pop closing quotation mark.
    return Token(TokenType.STRING, "".join(string))


def handle_escape(characters: CharacterQueue) -> str:
    if characters[0] in VALID_AFTER_BACKSLASH:
        return VALID_AFTER_BACKSLASH[characters.next()]
    elif characters[0] == 'u':
        return starts_with_unicode(characters)
    else:
        raise characters.error("Illegal escape character.")


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
            low_surrogate = extract_low_surrogate(characters)
            combined_code_point = combine_high_low_surrogates(code_point, low_surrogate)
            return chr(combined_code_point)

        return chr(int(code_point, 16))
    else:
        characters.error("Illegal unicode escape.")


def combine_high_low_surrogates(high_surrogate: str, low_surrogate: str) -> int:
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


def extract_low_surrogate(characters: CharacterQueue) -> str:
    first_six = characters.take(6)

    if re.match(r'\\u[a-fA-F0-9]{4}', first_six):
        code_point = first_six[2:]
        if is_low_surrogate(code_point) is False:
            characters.error("""Invalid codepoint after high surrogate.
            Only DC00-DFFF are valid low surrogates.""")
        else:
            return code_point
    else:
        characters.error("Couldn't find a unicode escape after high surrogate.")


def is_high_surrogate(code_point: str) -> bool:
    start = 0xD800
    end_inclusive = 0xDBFF
    return start <= int(code_point, 16) <= end_inclusive


def is_low_surrogate(code_point: str) -> bool:
    start = 0xDC00
    end_inclusive = 0xDFFF
    return start <= int(code_point, 16) <= end_inclusive
