from fredson_exceptions import FredsonParseError
from token_type import TokenType
from token_queue import TokenQueue


# What follows is a recursive descent parser that parses JSON according to the grammar
# found at www.json.org. Each function has a comment that indicates which grammar rule
# the function is tasked with parsing.
def parse_json(tokens: TokenQueue) -> dict:
    # json
    #     element
    try:
        return parse_element(tokens)
    except RecursionError:
        raise FredsonParseError("The JSON is too deeply nested.")


def parse_element(tokens: TokenQueue):
    # element
    #     ws value ws
    return parse_value(tokens)


def parse_value(tokens: TokenQueue):
    # value
    #     object
    #     array
    #     string
    #     number
    #     "true"
    #     "false"
    #     "null"
    if tokens.match(TokenType.LEFT_BRACE):
        return parse_object(tokens)
    elif tokens.match(TokenType.LEFT_BRACKET):
        return parse_array(tokens)
    elif tokens.match(TokenType.STRING):
        return parse_string(tokens)
    elif tokens.match(TokenType.DIGITS):
        return parse_number(tokens)
    elif tokens.match(TokenType.MINUS):
        return parse_number(tokens)
    elif tokens.match(TokenType.TRUE):
        return parse_true(tokens)
    elif tokens.match(TokenType.FALSE):
        return parse_false(tokens)
    elif tokens.match(TokenType.NULL):
        return parse_null(tokens)
    else:
        tokens.popleft("Expected start of a value such as a string or object", TokenType.LEFT_BRACE)


def parse_object(tokens) -> dict:
    # object
    #     '{' ws '}'
    #     '{' members '}'
    obj = {}
    left_brace = tokens.popleft("Expected '{'.", TokenType.LEFT_BRACE)

    if not tokens.match(TokenType.RIGHT_BRACE):
        members = parse_members(tokens)
        for member in members:
            obj.update(member)

    right_brace = tokens.popleft("Expected '}'", TokenType.RIGHT_BRACE)
    return obj


def parse_array(tokens: TokenQueue):
    # array
    #     '[' ws ']'
    #     '[' elements ']'
    left_bracket = tokens.popleft("Expected '['", TokenType.LEFT_BRACKET)
    elements = []

    if not tokens.match(TokenType.RIGHT_BRACKET):
        elements = parse_elements(tokens)

    right_bracket = tokens.popleft("Expected ']' or ','", TokenType.RIGHT_BRACKET)
    return elements


def parse_elements(tokens: TokenQueue):
    # elements
    #     element
    #     element ',' elements
    elements = [parse_element(tokens)]

    while tokens.match(TokenType.COMMA):
        comma = tokens.popleft()
        elements.append(parse_element(tokens))

    return elements


def parse_string(tokens: TokenQueue):
    # string
    #     '"' characters '"'
    string = tokens.popleft("Expected start of string", TokenType.STRING)
    return string.lexeme


def parse_number(tokens: TokenQueue):
    # number
    #     integer fraction exponent
    convert_to_float = False
    number = ""
    number += parse_integer(tokens)

    if tokens.match(TokenType.DOT):
        fraction = parse_fraction(tokens)
        if len(fraction) > 0:
            convert_to_float = True
        number += fraction

    if tokens.match(TokenType.EXPONENT):
        exponent = parse_exponent(tokens)
        if len(exponent) > 0:
            convert_to_float = True
        number += exponent

    return float(number) if convert_to_float else int(number)


def parse_integer(tokens: TokenQueue):
    # integer
    #     digit
    #     onenine digits
    #     '-' digit
    #     '-' onenine digits
    minus = ""
    integer = tokens.popleft("Expected integer", TokenType.DIGITS)
    return integer.lexeme if minus == "" else "-" + integer.lexeme


def parse_fraction(tokens: TokenQueue):
    # fraction
    #     ""
    #     '.' digits
    dot = tokens.popleft("Expected dot.", TokenType.DOT)
    digits = tokens.popleft("Expected digits after dot", TokenType.DIGITS, TokenType.ZERO_DIGITS)
    return dot.lexeme + digits.lexeme


def parse_exponent(tokens: TokenQueue):
    # exponent
    #     ""
    #     'E' sign digits
    #     'e' sign digits
    exponent = tokens.popleft().lexeme

    if tokens.match(TokenType.PLUS):
        exponent += tokens.popleft("Expected '+' or '-'", TokenType.PLUS, TokenType.MINUS).lexeme

    exponent += tokens.popleft("Expected digits", TokenType.DIGITS, TokenType.ZERO_DIGITS).lexeme
    return exponent


def parse_true(tokens: TokenQueue):
    true = tokens.popleft()
    return True


def parse_false(tokens: TokenQueue):
    false = tokens.popleft()
    return False


def parse_null(tokens):
    null = tokens.popleft()
    return None


def parse_members(tokens: TokenQueue):
    # members
    #     member
    #     member ',' members
    members = [parse_member(tokens)]

    while tokens.match(TokenType.COMMA):
        comma = tokens.popleft()
        members.append(parse_member(tokens))

    return members


def parse_member(tokens: TokenQueue):
    # member
    #     ws string ws ':' element
    string = parse_string(tokens)
    semi_colon = tokens.popleft("Expected ':'", TokenType.SEMICOLON)
    element = parse_element(tokens)
    return {string: element}

