def load_json_file(filename, encoding="utf8"):
    with open('seriot_test_suite/' + filename, encoding=encoding) as f:
        input_string = f.read()
    return input_string
    
