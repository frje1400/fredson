import os


def create_test_func(func_name, test_file):
    return f"""
def test_{func_name}():
    test_string = load_json_file('{test_file}')
    assert fredson_parse(test_string) == json.loads(test_string)
    
"""


file_names = os.listdir('seriot_test_suite')

with open('test_seriot_new.py', 'w') as f:
    f.write("import json")
    f.write("\n")
    f.write("from fredson import fredson_parse")
    f.write("\n")
    f.write("""
def load_json_file(filename):
    with open('seriot_test_suite/' + filename) as f:
        input_string = f.read()
    return input_string
    """)
    f.write("\n")
    f.write("\n")

    for name in file_names:
        func_name = name.replace('-', '_') if '-' in name else name
        func_name = func_name.replace('.', '_') if '.' in func_name else func_name
        func_name = func_name[:-5]
        func = create_test_func(func_name, name)
        f.write(func)

