from tokenizer import tokenize
from parser import parse_json

import json

def fredson_parse(raw_json: str) -> dict:
    tokens = tokenize(raw_json)
    parsed_json = parse_json(tokens)
    tokens.empty_after_parse()
    return parsed_json


if __name__ == '__main__':
    bad = '["\\uD801\\udc37"]'
    print(fredson_parse(bad))
    # print(json.loads(bad))
