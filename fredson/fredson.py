from tokenizer import tokenize
from json_parser import parse_json


def fredson_parse(raw_json: str) -> dict:
    tokens = tokenize(raw_json)
    parsed_json = parse_json(tokens)
    tokens.empty_after_parse()
    return parsed_json
