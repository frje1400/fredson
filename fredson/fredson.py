from tokenizer import tokenize
from json_parser import parse_json

import json


# The first 90 percent of the code accounts for the first 90 percent of the
# development time. The remaining 10 percent of the code accounts for the other
# 90 percent of the development time.
# -Tom Cargill, Bell Labs

def fredson_parse(raw_json: str) -> dict:
    tokens = tokenize(raw_json)
    parsed_json = parse_json(tokens)
    tokens.empty_after_parse()
    return parsed_json


if __name__ == '__main__':
    bad = '["\\uD801\\udc37"]'
    print(fredson_parse(bad))
    # print(json.loads(bad))
