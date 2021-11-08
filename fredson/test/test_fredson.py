import json

from fredson import fredson_parse


# Simple tests used during initial development.
# Built-in JSON module used as a reference implementation in some of these tests.


def test_parse_simple():
    simple = '{"foo":"bar"}'
    assert fredson_parse(simple) == {'foo': 'bar'}


def test_parse_nested():
    nested = '{"foo":{"bar":"baz"}}'
    assert fredson_parse(nested) == {'foo': {'bar': 'baz'}}


def test_parse_simple_list():
    simple_list = '{"foo": ["bar"]}'
    assert fredson_parse(simple_list) == {'foo': ['bar']}


def test_parse_two_item_list():
    two_items = '{"foo": ["bar", "baz"]}'
    assert fredson_parse(two_items) == {'foo': ['bar', 'baz']}


def test_parse_multi_line():
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


def test_parse_nested_lists():
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


def test_parse_multiple_keys():
    multiple_keys = """
    {
        "foo": "bar",
        "baz": "boo"
    }
    """
    assert fredson_parse(multiple_keys) == {'foo': 'bar', 'baz': 'boo'}, f"actual: {fredson_parse(multiple_keys)}"


def test_multiple_keys_nested_list():
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


def test_parse_simple_numbers():
    simple_numbers = """
    { "number": 123 }
    """
    assert fredson_parse(simple_numbers) == json.loads(simple_numbers)


def test_parse_simple_numbers_fraction():
    simple_numbers_fraction = """
    { "number": 123.456 }
    """
    assert fredson_parse(simple_numbers_fraction) == json.loads(simple_numbers_fraction)


def test_parse_fraction_exponent():
    simple_numbers_fraction_exponent = """ { "number": 123.456e+12 } """
    assert fredson_parse(simple_numbers_fraction_exponent) == json.loads(simple_numbers_fraction_exponent)


def test_parse_bool_false():
    false = """ { "bool": false } """
    assert fredson_parse(false) == json.loads(false)


def test_parse_bool_true():
    true = """ { "bool": true } """
    assert fredson_parse(true) == json.loads(true)


def test_parse_bool_null():
    null = """ { "bool": null } """
    assert fredson_parse(null) == json.loads(null)
