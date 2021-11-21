from fredson import fredson_parse
from time import perf_counter

filename = '10mb-sample.json'

with open(filename, encoding="utf8") as f:
    raw = f.read()

# t1 = perf_counter()
# fredson_parse(raw)
# t2 = perf_counter()
# print(f"{filename} parse in {t2-t1} seconds.")

import cProfile
cProfile.run('fredson_parse(raw)')