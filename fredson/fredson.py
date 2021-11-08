
from collections import deque
from tokenizer import tokenize, Token, TokenType


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