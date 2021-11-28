import json
from json import JSONDecodeError

import pytest

from fredson_exceptions import FredsonTokenError, FredsonParseError
from fredson import fredson_parse
from test_seriot import load_json_file


def test_i_number_double_huge_neg_exp():
    test_string = load_json_file('i_number_double_huge_neg_exp.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_number_huge_exp():
    test_string = load_json_file('i_number_huge_exp.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_number_neg_int_huge_exp():
    test_string = load_json_file('i_number_neg_int_huge_exp.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_number_pos_double_huge_exp():
    test_string = load_json_file('i_number_pos_double_huge_exp.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_number_real_neg_overflow():
    test_string = load_json_file('i_number_real_neg_overflow.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_number_real_pos_overflow():
    test_string = load_json_file('i_number_real_pos_overflow.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_number_real_underflow():
    test_string = load_json_file('i_number_real_underflow.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_number_too_big_neg_int():
    test_string = load_json_file('i_number_too_big_neg_int.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_number_too_big_pos_int():
    test_string = load_json_file('i_number_too_big_pos_int.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_number_very_big_negative_int():
    test_string = load_json_file('i_number_very_big_negative_int.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_object_key_lone_2nd_surrogate():
    test_string = load_json_file('i_object_key_lone_2nd_surrogate.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_1st_surrogate_but_2nd_missing():
    test_string = load_json_file('i_string_1st_surrogate_but_2nd_missing.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_1st_valid_surrogate_2nd_invalid():
    test_string = load_json_file('i_string_1st_valid_surrogate_2nd_invalid.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_incomplete_surrogates_escape_valid():
    test_string = load_json_file('i_string_incomplete_surrogates_escape_valid.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_incomplete_surrogate_and_escape_valid():
    test_string = load_json_file('i_string_incomplete_surrogate_and_escape_valid.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_incomplete_surrogate_pair():
    test_string = load_json_file('i_string_incomplete_surrogate_pair.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_invalid_lonely_surrogate():
    test_string = load_json_file('i_string_invalid_lonely_surrogate.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_invalid_surrogate():
    test_string = load_json_file('i_string_invalid_surrogate.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_invalid_utf_8():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('i_string_invalid_utf-8.json')


def test_i_string_inverted_surrogates_Uplus1D11E():
    test_string = load_json_file('i_string_inverted_surrogates_U+1D11E.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_iso_latin_1():
    test_string = load_json_file('i_string_iso_latin_1.json', encoding="latin1")
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_lone_second_surrogate():
    test_string = load_json_file('i_string_lone_second_surrogate.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_lone_utf8_continuation_byte():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('i_string_lone_utf8_continuation_byte.json')


def test_i_string_not_in_unicode_range():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('i_string_not_in_unicode_range.json')


def test_i_string_overlong_sequence_2_bytes():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('i_string_overlong_sequence_2_bytes.json')


def test_i_string_overlong_sequence_6_bytes():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('i_string_overlong_sequence_6_bytes.json')


def test_i_string_overlong_sequence_6_bytes_null():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('i_string_overlong_sequence_6_bytes_null.json')


def test_i_string_truncated_utf_8():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('i_string_truncated-utf-8.json')


def test_i_string_UTF_16LE_with_BOM():
    test_string = load_json_file('i_string_UTF-16LE_with_BOM.json', 'utf16')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_i_string_UTF_8_invalid_sequence():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('i_string_UTF-8_invalid_sequence.json')


def test_i_string_utf16BE_no_BOM():
    with pytest.raises(UnicodeError):
        test_string = load_json_file('i_string_utf16BE_no_BOM.json', 'utf16')


def test_i_string_utf16LE_no_BOM():
    with pytest.raises(UnicodeError):
        test_string = load_json_file('i_string_utf16LE_no_BOM.json', 'utf16')


def test_i_string_UTF8_surrogate_UplusD800():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('i_string_UTF8_surrogate_U+D800.json')


def test_i_structure_500_nested_arrays():
    # todo: it's legal according to rfc8295 to set a limit to the depth of nesting.
    # work on increasing this limit to be more compatible with python json?
    test_string = load_json_file('i_structure_500_nested_arrays.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)

    # can handle nesting 500 levels deep.
    json.loads(test_string)


def test_i_structure_UTF_8_BOM_empty_object():
    # todo: figure out what this actually tests.
    test_string = load_json_file('i_structure_UTF-8_BOM_empty_object.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)




