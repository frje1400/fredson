import json
import os
import re
import sys
import time

from enum import Enum, auto
from collections import deque


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


def fredson_parse(raw_json: str) -> dict:
    tokens = tokenize(raw_json)
    parsed_json = parse_json(tokens)
    return parsed_json


def parse_json(tokens):
    """
    json
        element
    """
    return parse_element(tokens)


def parse_element(tokens):
    """
    element
        ws value ws
    """
    return parse_value(tokens)


def parse_value(tokens):
    """
    value
        object
        array
        string
        number
        "true"
        "false"
        "null"
    """
    if tokens[0].token_type == TokenType.LEFT_BRACE:
        return parse_object(tokens)
    elif tokens[0].token_type == TokenType.LEFT_BRACKET:
        return parse_array(tokens)
    elif tokens[0].token_type == TokenType.STRING:
        return parse_string(tokens)
    elif tokens[0].token_type == TokenType.DIGITS:
        return parse_number(tokens)
    elif tokens[0].token_type == TokenType.MINUS:
        return parse_number(tokens)
    elif tokens[0].token_type == TokenType.TRUE:
        return parse_true(tokens)
    elif tokens[0].token_type == TokenType.FALSE:
        return parse_false(tokens)
    elif tokens[0].token_type == TokenType.NULL:
        return parse_null(tokens)


def parse_object(tokens: deque[Token]) -> dict:
    """
    object
        '{' ws '}'
        '{' members '}'
    """
    obj = {}

    if tokens[0].token_type != TokenType.LEFT_BRACE:
        raise Exception(f"parse_object must start with left brace {tokens[0]}")

    tokens.popleft()  # pop left brace.

    members = parse_members(tokens)
    for member in members:
        obj.update(member)

    if tokens[0].token_type != TokenType.RIGHT_BRACE:
        raise Exception(f"Missing right brace after value: {tokens[0]}")

    tokens.popleft()

    return obj


def parse_array(tokens):
    """
    array
        '[' ws ']'
        '[' elements ']'
    """
    if tokens[0].token_type != TokenType.LEFT_BRACKET:
        raise Exception(f"parse_array must start with left bracket {tokens[0]}")

    tokens.popleft()  # pop left bracket.

    elements = parse_elements(tokens)

    if tokens[0].token_type != TokenType.RIGHT_BRACKET:
        raise Exception(f"Missing right bracket after elements parse_array: {tokens[0]}")

    tokens.popleft()  # pop right bracket.

    return elements


def parse_elements(tokens):
    """
    elements
        element
        element ',' elements
    """
    element = parse_element(tokens)

    elements = []
    while tokens[0].token_type == TokenType.COMMA:
        tokens.popleft()  # remove comma.
        elements = parse_elements(tokens)

    return [element, *elements]


def parse_string(tokens):
    """
    string
        '"' characters '"'
    """
    if tokens[0].token_type != TokenType.STRING:
        raise Exception('Not TokenType STRING in parse_string.')

    token = tokens.popleft()
    return token.lexeme


def parse_number(tokens):
    """
    number
        integer fraction exponent
    """
    convert_to_float = False
    number = ""
    number += parse_integer(tokens)

    if tokens[0].token_type == TokenType.DOT:
        fraction = parse_fraction(tokens)
        if len(fraction) > 0:
            convert_to_float = True
        number += fraction

    if tokens[0].token_type == TokenType.EXPONENT:
        exponent = parse_exponent(tokens)
        if len(exponent) > 0:
            convert_to_float = True
        number += exponent

    return float(number) if convert_to_float else int(number)


def parse_integer(tokens):
    """
    integer
        digit
        onenine digits
        '-' digit
        '-' onenine digits
    """
    minus = ""
    if tokens[0].token_type == TokenType.MINUS:
        minus = tokens.popleft()

    if tokens[0].token_type != TokenType.DIGITS:
        raise Exception('Not digits in parse_integer.')

    integer = tokens.popleft()
    return integer.lexeme if minus == "" else "-" + integer.lexeme


def parse_fraction(tokens):
    """
    fraction
        ""
        '.' digits
    """
    dot = tokens.popleft()

    if tokens[0].token_type != TokenType.DIGITS and tokens[0].token_type != TokenType.ZERO_DIGITS:
        raise Exception('parse_fraction: missing digits after dot.')

    digits = tokens.popleft()
    return dot.lexeme + digits.lexeme


def parse_exponent(tokens):
    """
    exponent
        ""
        'E' sign digits
        'e' sign digits
    """
    exponent = tokens.popleft().lexeme

    if tokens[0].token_type == TokenType.PLUS or tokens[0].token_type == TokenType.MINUS:
        exponent += tokens.popleft().lexeme

    if tokens[0].token_type != TokenType.DIGITS and tokens[0].token_type != TokenType.ZERO_DIGITS:
        raise Exception('parse_exponent: missing digits.')

    exponent += tokens.popleft().lexeme
    return exponent


def parse_true(tokens):
    true_token = tokens.popleft()
    return True


def parse_false(tokens):
    false_token = tokens.popleft()
    return False


def parse_null(tokens):
    null_token = tokens.popleft()
    return None


def parse_members(tokens):
    """
    members
        member
        member ',' members
    """
    member = parse_member(tokens)

    members = []
    while tokens[0].token_type == TokenType.COMMA:
        tokens.popleft()  # remove comma.
        members = parse_members(tokens)

    return [member, *members]


def parse_member(tokens):
    """
    member
        ws string ws ':' element
    """
    if tokens[0].token_type != TokenType.STRING:
        raise Exception('Missing string in parse_member')

    string = parse_string(tokens)

    if tokens[0].token_type != TokenType.SEMICOLON:
        raise Exception('Missing semicolon in parse_member')

    tokens.popleft()  # remove semicolon.

    element = parse_element(tokens)

    return {string: element}


simple = '{"foo":"bar"}'
assert fredson_parse(simple) == {'foo': 'bar'}

nested = '{"foo":{"bar":"baz"}}'
assert fredson_parse(nested) == {'foo': {'bar': 'baz'}}

simple_list = '{"foo": ["bar"]}'
assert fredson_parse(simple_list) == {'foo': ['bar']}, f"actual: {fredson_parse(simple_list)}"

listed = '{"foo": ["bar", "baz"]}'
assert fredson_parse(listed) == {'foo': ['bar', 'baz']}

multi_line = """
{
"foo":
    [
    "bar",
    "baz"
    ]
}
"""
assert fredson_parse(multi_line) == {'foo': ['bar', 'baz']}

nested_lists = """
{
  "foo": [
    {
      "bar": [
        "baz",
        "qxc",
        "abc"
      ]
    }
  ]
}
"""
assert fredson_parse(nested_lists) == {'foo': [{'bar': ['baz', 'qxc', 'abc']}]}


multiple_keys = """
{
    "foo": "bar",
    "baz": "boo"
}
"""
assert fredson_parse(multiple_keys) == {'foo': 'bar', 'baz': 'boo'}, f"actual: {fredson_parse(multiple_keys)}"

multiple_keys_nested_list = """
{
  "foo": [
    {
      "bar": [
        "baz",
        "qxc",
        "abc"
      ]
    }
  ],
  "uvw": "qxas",
  "vghj": "nja",
  "oasfa": {
    "asc": "asarera",
    "dgdjkj": "deijij",
    "iuiuij": "hihih"
  }
}
"""
assert fredson_parse(multiple_keys_nested_list) == json.loads(multiple_keys_nested_list)

simple_numbers = """
{ "number": 123 }
"""

assert fredson_parse(simple_numbers) == json.loads(simple_numbers), f"actual: {fredson_parse(simple_numbers)}"

simple_numbers_fraction = """
{ "number": 123.456 }
"""
assert fredson_parse(simple_numbers_fraction) == json.loads(simple_numbers_fraction),\
    f"actual: {fredson_parse(simple_numbers_fraction)}"


simple_numbers_fraction_exponent = """
{ "number": 123.456e+12 }
"""
assert fredson_parse(simple_numbers_fraction_exponent) == json.loads(simple_numbers_fraction_exponent), \
    f"actual: {fredson_parse(simple_numbers_fraction_exponent)}"

false = """
{ "bool": false }
"""
assert fredson_parse(false) == json.loads(false), \
    f"actual: {fredson_parse(false)}"

true = """
{ "bool": true }
"""
assert fredson_parse(true) == json.loads(true), \
    f"actual: {fredson_parse(true)}"

null = """
{ "bool": null }
"""
assert fredson_parse(null) == json.loads(null), \
    f"actual: {fredson_parse(null)}"
