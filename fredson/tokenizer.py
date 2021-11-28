import re

from collections import deque
from fredson_exceptions import FredsonTokenError
from token_type import TokenType
from token_queue import TokenQueue, Token
from typing import Optional, Callable


class LookupTable:
    simple_tokens: dict[str, TokenType]
    keywords: dict[str, TokenType]
    valid_after_backslash: dict[str, str]
    valid_whitespace: set[str]
    digits: set[str]
    digits_and_dash: set[str]
    letters_A_Z: set[str]
    letters_a_z: set[str]
    letter: set[str]
    start_of_keyword: set[str]
    illegal_control_character: set[str]
    string_termination: set[str]
    first_char: dict[str, Callable]

    def __init__(self):
        self.simple_tokens = {
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

        self.keywords = {
            'true': TokenType.TRUE,
            'false': TokenType.FALSE,
            'null': TokenType.NULL
        }

        self.valid_after_backslash = {
            '\"': '\"',
            '\\': '\\',
            '/': '/',
            'b': '\b',
            'f': '\f',
            'n': '\n',
            'r': '\r',
            't': '\t'
        }

        self.valid_whitespace = {' ', '\n', '\r', '\t'}
        self.digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        self.digits_and_dash = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"}
        self.letters_A_Z = {chr(i) for i in range(65, 91)}
        self.letters_a_z = {chr(i) for i in range(97, 123)}
        self.letters = self.letters_A_Z.union(self.letters_a_z)
        self.start_of_keyword = {'t', 'f', 'n'}
        self.illegal_control_characters = {chr(n) for n in range(32)}
        self.string_termination = {'"', '\\', *{illegal for illegal in self.illegal_control_characters}}

        # Maps from a character to the function that handles that character.
        self.first_char = {}

        # Tokens that are defined as simple tokens consist of a single character, e.g.
        # '{' and '['.
        for simple_token in self.simple_tokens:
            self.first_char[simple_token] = tokenize_simple_token
        # A number starts with [0-9] or -
        for digit in self.digits_and_dash:
            self.first_char[digit] = tokenize_number
        # Only a limited number of white space characters are allowed in JSON.
        for white in self.valid_whitespace:
            self.first_char[white] = tokenize_whitespace
        # A keyword must start with 'f', 't' or 'n' (false, null and true).
        for char in self.start_of_keyword:
            self.first_char[char] = tokenize_keyword

        # A string must start with "
        self.first_char['"'] = tokenize_json_string

        # The plus sign is handled differently than other simple tokens.
        self.first_char['+'] = tokenize_plus_sign


def tokenize(raw_json) -> TokenQueue:
    tokens = deque()
    start_index = 0
    length = len(raw_json)
    lookup_table = LookupTable()

    while start_index < length:
        try:
            # The main loop of the tokenizer has a finite number of characters that it needs
            # to look at to decide what to do next. It's faster to decide what to do next by
            # looking up the character in a dictionary rather than using a series of if/else
            # statements using the first character.
            current = raw_json[start_index]
            func = lookup_table.first_char[current]
            token, end_index = func(raw_json, start_index, length, lookup_table)
            tokens.append(token)
            start_index = end_index + 1
        except KeyError:
            token_error(raw_json, f"Invalid char: {raw_json[start_index]}", start_index)
        except IndexError:
            error_message = "Unexpectedly reached the end of the input string." \
                            "Did you forget to terminate a string?"
            token_error(raw_json, error_message, start_index)

    return TokenQueue(tokens)


def token_error(characters: str, message: str, current_index: int) -> None:
    total_length = len(characters)
    remaining = total_length - current_index
    chars_to_grab = remaining if remaining < 20 else 20
    json_chunk = characters[current_index: current_index + chars_to_grab] \
        if total_length > 20 else characters

    error_message = f"{json_chunk}  <-\n\n{message}"
    raise FredsonTokenError(error_message)


def tokenize_simple_token(characters: str, current_index: int, length: int,
                          lookup_table: LookupTable) -> (Token, int):
    char = characters[current_index]
    return Token(lookup_table.simple_tokens[char], char), current_index


def tokenize_whitespace(characters: str, current_index: int, length: int,
                        lookup_table: LookupTable) -> (Token, int):
    return Token(TokenType.WHITESPACE, characters[current_index]), current_index


def tokenize_plus_sign(characters: str, current_index: int, length: int,
                       lookup_table: LookupTable) -> (Token, int):
    if (current_index + 1 == length) or characters[current_index + 1] not in lookup_table.digits:
        token_error(characters, "Plus sign must be followed by [0-9]", current_index)
    return Token(TokenType.PLUS, '+'), current_index


def tokenize_keyword(characters: str, current_index: int, length: int,
                     lookup_table: LookupTable) -> (Token, int):
    word_characters = []

    while current_index < length:
        char = characters[current_index]
        if char in lookup_table.letters_a_z:
            word_characters.append(char)
            current_index += 1
        else:
            break

    word = "".join(word_characters)

    if word in lookup_table.keywords:
        return Token(lookup_table.keywords[word], word), current_index - 1
    else:
        token_error(characters, f"Illegal keyword '{word}'", current_index)


def tokenize_number(characters: str, current_index: int, length: int,
                    lookup_table: LookupTable) -> (Token, int):
    number_chars = [characters[current_index]]
    current_index += 1

    while current_index < length and characters[current_index] in lookup_table.digits:
        number_chars.append(characters[current_index])
        current_index += 1

    num = "".join(number_chars)
    token = validate_number(num, characters, current_index)
    return token, current_index - 1


def validate_number(num: str, characters: str, current_index: int) -> Token:
    if num.startswith("-") and len(num) == 1:
        token_error(characters, "Found single minus sign without number.", current_index)
    elif num.startswith("-") and len(num) > 2 and num[1] == "0":
        token_error(characters, "Found starting 0 in a number that starts with minus sign.",
                    current_index)
    elif num.startswith("0") and len(num) > 1:
        return Token(TokenType.ZERO_DIGITS, num)
    else:
        return Token(TokenType.DIGITS, num)


def tokenize_json_string(characters: str, current_index: int, length: int,
                         lookup_table: LookupTable) -> (Token, int):
    current_index += 1  # ignore opening "
    chars_in_string = []

    char = characters[current_index]
    while char not in lookup_table.string_termination:
        chars_in_string.append(char)
        current_index += 1
        char = characters[current_index]

    string = "".join(chars_in_string)

    if characters[current_index] == '"':
        # "fast" path; "easy" string with no escapes or control characters.
        return Token(TokenType.STRING, string), current_index
    else:
        return slow_string(characters, string, current_index, lookup_table)


def slow_string(characters: str, partial_string: str, current_index: int,
                lookup_table: LookupTable) -> (Token, int):
    string = [partial_string]

    while characters[current_index] != '"':
        char = characters[current_index]

        # Characters U+0000 (0) through U+001F (31) are control characters that must be
        # escaped. If we find such a character here, before we have seen a \, that is an
        # illegal character.
        if char in lookup_table.illegal_control_characters:
            token_error(characters, f"Illegal control character: {char}", current_index)
        elif char == "\\":
            next_char, end_index = handle_escape(characters, current_index + 1, lookup_table)
            current_index = end_index
            string.append(next_char)
        else:
            string.append(char)
            current_index += 1

    return Token(TokenType.STRING, "".join(string)), current_index


def handle_escape(characters, current_index: int, lookup_table: LookupTable) -> (str, int):
    char = characters[current_index]

    if char in lookup_table.valid_after_backslash:
        return lookup_table.valid_after_backslash[char], current_index + 1
    elif char == 'u':
        return starts_with_unicode(characters, current_index + 1, lookup_table)
    else:
        token_error(characters, f"Illegal escape character: {char}", current_index)


def starts_with_unicode(characters: str, current_index: int,
                        lookup_table: LookupTable) -> (str, int):
    """If the characters start with u[a-fA-F0-9]{4} this method uses the four
    hex digits to return the corresponding character.

    Example: if the characters start with u0063, this method will return 'c'
    because chr(int('0063', 16)) -> 'c'.
    """
    code_point = characters[current_index: current_index + 4]

    # u_hex_hex_hex_hex = r'u[a-fA-F0-9]{4}'
    hex_hex_hex_hex = re.compile(r'[a-fA-F0-9]{4}')

    if re.match(hex_hex_hex_hex, code_point):
        if is_high_surrogate(code_point):
            print(f"code_point: {code_point}")
            # A high surrogate must be followed by a low surrogate. The high and low
            # surrogates are then combined to create a code point that is bigger than
            # 16 bits. This is looks strange but its purpose is to allow JSON to express
            # unicode using the unicode escape syntax (\u_hex_hex_hex_hex) while
            # simultaneously only using 16 bits per code point to stay compatible with
            # utf-16.
            return combine_high_low_surrogates(characters, current_index + 4, code_point)

        return chr(int(code_point, 16)), current_index + 4
    else:
        token_error(characters, f"Illegal unicode escape: {code_point}", current_index)


def combine_high_low_surrogates(characters: str, current_index: int,
                                high_surrogate: str) -> (str, int):
    low_surrogate_candidate, end_index = extract_low_surrogate(characters, current_index)

    if low_surrogate_candidate is None:
        # If we don't have a matching low surrogate the behavior of the builtin JSON module
        # is to return only the high surrogate.
        return chr(int(high_surrogate, 16)), end_index

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
        return (chr(int(high_surrogate, 16)) + chr(int(low_surrogate_candidate, 16))), end_index

    combined_code_point = high_low_surrogate_algorithm(high_surrogate, low_surrogate_candidate)
    return chr(combined_code_point), end_index


def extract_low_surrogate(characters: str, current_index: int) -> (Optional[str], int):
    low_surrogate_candidate = characters[current_index: current_index + 6]

    if re.match(r'\\u[a-fA-F0-9]{4}', low_surrogate_candidate):
        code_point = low_surrogate_candidate[2:]
        return "".join(code_point), current_index + 6
    else:
        return None, current_index


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


if __name__ == '__main__':
    toks = tokenize('[-]')
    for t in toks:
        print(t)
