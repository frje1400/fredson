from fredson import fredson_parse
from time import perf_counter

import json

filename = 'large-file.json'

with open(filename, encoding="utf8") as f:
    raw = f.read()

t1 = perf_counter()
fredson_parse(raw)
t2 = perf_counter()
print(f"{filename} parse in {t2-t1} seconds.")
