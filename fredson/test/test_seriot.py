import json
from json import JSONDecodeError

import pytest

from definitions import FredsonParseError, FredsonTokenError
from fredson import fredson_parse

def load_json_file(filename):
    with open('seriot_test_suite/' + filename, encoding="utf8") as f:
        input_string = f.read()
    return input_string
    

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
    test_string = load_json_file('i_string_invalid_utf-8.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_i_string_inverted_surrogates_U+1D11E():
#     test_string = load_json_file('i_string_inverted_surrogates_U+1D11E.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_iso_latin_1():
    test_string = load_json_file('i_string_iso_latin_1.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_lone_second_surrogate():
    test_string = load_json_file('i_string_lone_second_surrogate.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# todo: get unicodedecodeerror just opening this file.
def test_i_string_lone_utf8_continuation_byte():
    # test_string = load_json_file('i_string_lone_utf8_continuation_byte.json')
    # fred = fredson_parse(test_string)
    # py = json.loads(test_string)
    # print(fred)
    pass
    

def test_i_string_not_in_unicode_range():
    test_string = load_json_file('i_string_not_in_unicode_range.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_overlong_sequence_2_bytes():
    test_string = load_json_file('i_string_overlong_sequence_2_bytes.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_overlong_sequence_6_bytes():
    test_string = load_json_file('i_string_overlong_sequence_6_bytes.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_overlong_sequence_6_bytes_null():
    test_string = load_json_file('i_string_overlong_sequence_6_bytes_null.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_truncated_utf_8():
    test_string = load_json_file('i_string_truncated-utf-8.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_UTF_16LE_with_BOM():
    test_string = load_json_file('i_string_UTF-16LE_with_BOM.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_UTF_8_invalid_sequence():
    test_string = load_json_file('i_string_UTF-8_invalid_sequence.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_utf16BE_no_BOM():
    test_string = load_json_file('i_string_utf16BE_no_BOM.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_string_utf16LE_no_BOM():
    test_string = load_json_file('i_string_utf16LE_no_BOM.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_i_string_UTF8_surrogate_U+D800():
#     test_string = load_json_file('i_string_UTF8_surrogate_U+D800.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_structure_500_nested_arrays():
    test_string = load_json_file('i_structure_500_nested_arrays.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_i_structure_UTF_8_BOM_empty_object():
    test_string = load_json_file('i_structure_UTF-8_BOM_empty_object.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_array_1_true_without_comma():
    test_string = load_json_file('n_array_1_true_without_comma.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_array_a_invalid_utf8():
    test_string = load_json_file('n_array_a_invalid_utf8.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_array_colon_instead_of_comma():
    test_string = load_json_file('n_array_colon_instead_of_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)
    

def test_n_array_comma_after_close():
    test_string = load_json_file('n_array_comma_after_close.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_comma_and_number():
    test_string = load_json_file('n_array_comma_and_number.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_double_comma():
    test_string = load_json_file('n_array_double_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_double_extra_comma():
    test_string = load_json_file('n_array_double_extra_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_extra_close():
    test_string = load_json_file('n_array_extra_close.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_extra_comma():
    test_string = load_json_file('n_array_extra_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_incomplete():
    test_string = load_json_file('n_array_incomplete.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_incomplete_invalid_value():
    test_string = load_json_file('n_array_incomplete_invalid_value.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_inner_array_no_comma():
    test_string = load_json_file('n_array_inner_array_no_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


# todo: Don't know what to do with this since it doesn't even decode the file.
# def test_n_array_invalid_utf8():
#     test_string = load_json_file('n_array_invalid_utf8.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_array_items_separated_by_semicolon():
    test_string = load_json_file('n_array_items_separated_by_semicolon.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_just_comma():
    test_string = load_json_file('n_array_just_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_just_minus():
    test_string = load_json_file('n_array_just_minus.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_missing_value():
    test_string = load_json_file('n_array_missing_value.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_newlines_unclosed():
    test_string = load_json_file('n_array_newlines_unclosed.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_number_and_comma():
    test_string = load_json_file('n_array_number_and_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_number_and_several_commas():
    test_string = load_json_file('n_array_number_and_several_commas.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_spaces_vertical_tab_formfeed():
    test_string = load_json_file('n_array_spaces_vertical_tab_formfeed.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_star_inside():
    test_string = load_json_file('n_array_star_inside.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_unclosed():
    test_string = load_json_file('n_array_unclosed.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_unclosed_trailing_comma():
    test_string = load_json_file('n_array_unclosed_trailing_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_unclosed_with_new_lines():
    test_string = load_json_file('n_array_unclosed_with_new_lines.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_array_unclosed_with_object_inside():
    test_string = load_json_file('n_array_unclosed_with_object_inside.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)
    with pytest.raises(JSONDecodeError):
        json.loads(test_string)


def test_n_incomplete_false():
    test_string = load_json_file('n_incomplete_false.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_incomplete_null():
    test_string = load_json_file('n_incomplete_null.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_incomplete_true():
    test_string = load_json_file('n_incomplete_true.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_multidigit_number_then_00():
    test_string = load_json_file('n_multidigit_number_then_00.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_number_++():
#     test_string = load_json_file('n_number_++.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_n_number_+1():
#     test_string = load_json_file('n_number_+1.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_n_number_+Inf():
#     test_string = load_json_file('n_number_+Inf.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number__01():
    test_string = load_json_file('n_number_-01.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number__1_0_():
    test_string = load_json_file('n_number_-1.0..json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number__2_():
    test_string = load_json_file('n_number_-2..json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number__NaN():
    test_string = load_json_file('n_number_-NaN.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number___1():
    test_string = load_json_file('n_number_.-1.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number__2e_3():
    test_string = load_json_file('n_number_.2e-3.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_0_1_2():
    test_string = load_json_file('n_number_0.1.2.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_number_0_3e+():
#     test_string = load_json_file('n_number_0.3e+.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#

def test_n_number_0_3e():
    test_string = load_json_file('n_number_0.3e.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_0_e1():
    test_string = load_json_file('n_number_0.e1.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_number_0e+():
#     test_string = load_json_file('n_number_0e+.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_0e():
    test_string = load_json_file('n_number_0e.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_number_0_capital_E+():
#     test_string = load_json_file('n_number_0_capital_E+.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_0_capital_E():
    test_string = load_json_file('n_number_0_capital_E.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_number_1_0e+():
#     test_string = load_json_file('n_number_1.0e+.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_1_0e_():
    test_string = load_json_file('n_number_1.0e-.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_1_0e():
    test_string = load_json_file('n_number_1.0e.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_1eE2():
    test_string = load_json_file('n_number_1eE2.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_1_000():
    test_string = load_json_file('n_number_1_000.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_number_2_e+3():
#     test_string = load_json_file('n_number_2.e+3.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_2_e_3():
    test_string = load_json_file('n_number_2.e-3.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_2_e3():
    test_string = load_json_file('n_number_2.e3.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_number_9_e+():
#     test_string = load_json_file('n_number_9.e+.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_expression():
    test_string = load_json_file('n_number_expression.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_hex_1_digit():
    test_string = load_json_file('n_number_hex_1_digit.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_hex_2_digits():
    test_string = load_json_file('n_number_hex_2_digits.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_Inf():
    test_string = load_json_file('n_number_Inf.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_infinity():
    test_string = load_json_file('n_number_infinity.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_number_invalid+_():
#     test_string = load_json_file('n_number_invalid+-.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_invalid_negative_real():
    test_string = load_json_file('n_number_invalid-negative-real.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_invalid_utf_8_in_bigger_int():
    test_string = load_json_file('n_number_invalid-utf-8-in-bigger-int.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_invalid_utf_8_in_exponent():
    test_string = load_json_file('n_number_invalid-utf-8-in-exponent.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_invalid_utf_8_in_int():
    test_string = load_json_file('n_number_invalid-utf-8-in-int.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_minus_infinity():
    test_string = load_json_file('n_number_minus_infinity.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_minus_sign_with_trailing_garbage():
    test_string = load_json_file('n_number_minus_sign_with_trailing_garbage.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_minus_space_1():
    test_string = load_json_file('n_number_minus_space_1.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_NaN():
    test_string = load_json_file('n_number_NaN.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_neg_int_starting_with_zero():
    test_string = load_json_file('n_number_neg_int_starting_with_zero.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_neg_real_without_int_part():
    test_string = load_json_file('n_number_neg_real_without_int_part.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_neg_with_garbage_at_end():
    test_string = load_json_file('n_number_neg_with_garbage_at_end.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_real_garbage_after_e():
    test_string = load_json_file('n_number_real_garbage_after_e.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_real_without_fractional_part():
    test_string = load_json_file('n_number_real_without_fractional_part.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_real_with_invalid_utf8_after_e():
    test_string = load_json_file('n_number_real_with_invalid_utf8_after_e.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_starting_with_dot():
    test_string = load_json_file('n_number_starting_with_dot.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_number_U+FF11_fullwidth_digit_one():
#     test_string = load_json_file('n_number_U+FF11_fullwidth_digit_one.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_with_alpha():
    test_string = load_json_file('n_number_with_alpha.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_with_alpha_char():
    test_string = load_json_file('n_number_with_alpha_char.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_number_with_leading_zero():
    test_string = load_json_file('n_number_with_leading_zero.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_bad_value():
    test_string = load_json_file('n_object_bad_value.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_bracket_key():
    test_string = load_json_file('n_object_bracket_key.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_comma_instead_of_colon():
    test_string = load_json_file('n_object_comma_instead_of_colon.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_double_colon():
    test_string = load_json_file('n_object_double_colon.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_emoji():
    test_string = load_json_file('n_object_emoji.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_garbage_at_end():
    test_string = load_json_file('n_object_garbage_at_end.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_key_with_single_quotes():
    test_string = load_json_file('n_object_key_with_single_quotes.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_lone_continuation_byte_in_key_and_trailing_comma():
    test_string = load_json_file('n_object_lone_continuation_byte_in_key_and_trailing_comma.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_missing_colon():
    test_string = load_json_file('n_object_missing_colon.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_missing_key():
    test_string = load_json_file('n_object_missing_key.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_missing_semicolon():
    test_string = load_json_file('n_object_missing_semicolon.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_missing_value():
    test_string = load_json_file('n_object_missing_value.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_no_colon():
    test_string = load_json_file('n_object_no-colon.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_non_string_key():
    test_string = load_json_file('n_object_non_string_key.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_non_string_key_but_huge_number_instead():
    test_string = load_json_file('n_object_non_string_key_but_huge_number_instead.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_repeated_null_null():
    test_string = load_json_file('n_object_repeated_null_null.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_several_trailing_commas():
    test_string = load_json_file('n_object_several_trailing_commas.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_single_quote():
    test_string = load_json_file('n_object_single_quote.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_trailing_comma():
    test_string = load_json_file('n_object_trailing_comma.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_trailing_comment():
    test_string = load_json_file('n_object_trailing_comment.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_trailing_comment_open():
    test_string = load_json_file('n_object_trailing_comment_open.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_trailing_comment_slash_open():
    test_string = load_json_file('n_object_trailing_comment_slash_open.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_trailing_comment_slash_open_incomplete():
    test_string = load_json_file('n_object_trailing_comment_slash_open_incomplete.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_two_commas_in_a_row():
    test_string = load_json_file('n_object_two_commas_in_a_row.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_unquoted_key():
    test_string = load_json_file('n_object_unquoted_key.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_unterminated_value():
    test_string = load_json_file('n_object_unterminated-value.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_with_single_string():
    test_string = load_json_file('n_object_with_single_string.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_object_with_trailing_garbage():
    test_string = load_json_file('n_object_with_trailing_garbage.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_single_space():
    test_string = load_json_file('n_single_space.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_1_surrogate_then_escape():
    test_string = load_json_file('n_string_1_surrogate_then_escape.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_1_surrogate_then_escape_u():
    test_string = load_json_file('n_string_1_surrogate_then_escape_u.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_1_surrogate_then_escape_u1():
    test_string = load_json_file('n_string_1_surrogate_then_escape_u1.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_1_surrogate_then_escape_u1x():
    test_string = load_json_file('n_string_1_surrogate_then_escape_u1x.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_accentuated_char_no_quotes():
    test_string = load_json_file('n_string_accentuated_char_no_quotes.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_backslash_00():
    test_string = load_json_file('n_string_backslash_00.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_escaped_backslash_bad():
    test_string = load_json_file('n_string_escaped_backslash_bad.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_escaped_ctrl_char_tab():
    test_string = load_json_file('n_string_escaped_ctrl_char_tab.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_escaped_emoji():
    test_string = load_json_file('n_string_escaped_emoji.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_escape_x():
    test_string = load_json_file('n_string_escape_x.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_incomplete_escape():
    test_string = load_json_file('n_string_incomplete_escape.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_incomplete_escaped_character():
    test_string = load_json_file('n_string_incomplete_escaped_character.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_incomplete_surrogate():
    test_string = load_json_file('n_string_incomplete_surrogate.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_incomplete_surrogate_escape_invalid():
    test_string = load_json_file('n_string_incomplete_surrogate_escape_invalid.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_invalid_utf_8_in_escape():
    test_string = load_json_file('n_string_invalid-utf-8-in-escape.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_invalid_backslash_esc():
    test_string = load_json_file('n_string_invalid_backslash_esc.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_invalid_unicode_escape():
    test_string = load_json_file('n_string_invalid_unicode_escape.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_invalid_utf8_after_escape():
    test_string = load_json_file('n_string_invalid_utf8_after_escape.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_leading_uescaped_thinspace():
    test_string = load_json_file('n_string_leading_uescaped_thinspace.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_no_quotes_with_bad_escape():
    test_string = load_json_file('n_string_no_quotes_with_bad_escape.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_single_doublequote():
    test_string = load_json_file('n_string_single_doublequote.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_single_quote():
    test_string = load_json_file('n_string_single_quote.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_single_string_no_double_quotes():
    test_string = load_json_file('n_string_single_string_no_double_quotes.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_start_escape_unclosed():
    test_string = load_json_file('n_string_start_escape_unclosed.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_unescaped_ctrl_char():
    test_string = load_json_file('n_string_unescaped_ctrl_char.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_unescaped_newline():
    test_string = load_json_file('n_string_unescaped_newline.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_unescaped_tab():
    test_string = load_json_file('n_string_unescaped_tab.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_unicode_CapitalU():
    test_string = load_json_file('n_string_unicode_CapitalU.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_string_with_trailing_garbage():
    test_string = load_json_file('n_string_with_trailing_garbage.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_100000_opening_arrays():
    test_string = load_json_file('n_structure_100000_opening_arrays.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_angle_bracket__():
    test_string = load_json_file('n_structure_angle_bracket_..json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_angle_bracket_null():
    test_string = load_json_file('n_structure_angle_bracket_null.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_array_trailing_garbage():
    test_string = load_json_file('n_structure_array_trailing_garbage.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_array_with_extra_array_close():
    test_string = load_json_file('n_structure_array_with_extra_array_close.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_array_with_unclosed_string():
    test_string = load_json_file('n_structure_array_with_unclosed_string.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_ascii_unicode_identifier():
    test_string = load_json_file('n_structure_ascii-unicode-identifier.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_capitalized_True():
    test_string = load_json_file('n_structure_capitalized_True.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_close_unopened_array():
    test_string = load_json_file('n_structure_close_unopened_array.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_comma_instead_of_closing_brace():
    test_string = load_json_file('n_structure_comma_instead_of_closing_brace.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_double_array():
    test_string = load_json_file('n_structure_double_array.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_end_array():
    test_string = load_json_file('n_structure_end_array.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_incomplete_UTF8_BOM():
    test_string = load_json_file('n_structure_incomplete_UTF8_BOM.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_lone_invalid_utf_8():
    test_string = load_json_file('n_structure_lone-invalid-utf-8.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_lone_open_bracket():
    test_string = load_json_file('n_structure_lone-open-bracket.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_no_data():
    test_string = load_json_file('n_structure_no_data.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_null_byte_outside_string():
    test_string = load_json_file('n_structure_null-byte-outside-string.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_number_with_trailing_garbage():
    test_string = load_json_file('n_structure_number_with_trailing_garbage.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_object_followed_by_closing_object():
    test_string = load_json_file('n_structure_object_followed_by_closing_object.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_object_unclosed_no_value():
    test_string = load_json_file('n_structure_object_unclosed_no_value.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_object_with_comment():
    test_string = load_json_file('n_structure_object_with_comment.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_object_with_trailing_garbage():
    test_string = load_json_file('n_structure_object_with_trailing_garbage.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_array_apostrophe():
    test_string = load_json_file('n_structure_open_array_apostrophe.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_array_comma():
    test_string = load_json_file('n_structure_open_array_comma.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_array_object():
    test_string = load_json_file('n_structure_open_array_object.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_array_open_object():
    test_string = load_json_file('n_structure_open_array_open_object.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_array_open_string():
    test_string = load_json_file('n_structure_open_array_open_string.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_array_string():
    test_string = load_json_file('n_structure_open_array_string.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_object():
    test_string = load_json_file('n_structure_open_object.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_object_close_array():
    test_string = load_json_file('n_structure_open_object_close_array.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_object_comma():
    test_string = load_json_file('n_structure_open_object_comma.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_object_open_array():
    test_string = load_json_file('n_structure_open_object_open_array.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_object_open_string():
    test_string = load_json_file('n_structure_open_object_open_string.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_object_string_with_apostrophes():
    test_string = load_json_file('n_structure_open_object_string_with_apostrophes.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_open_open():
    test_string = load_json_file('n_structure_open_open.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_single_eacute():
    test_string = load_json_file('n_structure_single_eacute.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_single_star():
    test_string = load_json_file('n_structure_single_star.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_structure_trailing_#():
#     test_string = load_json_file('n_structure_trailing_#.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_n_structure_U+2060_word_joined():
#     test_string = load_json_file('n_structure_U+2060_word_joined.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#

def test_n_structure_uescaped_LF_before_string():
    test_string = load_json_file('n_structure_uescaped_LF_before_string.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_unclosed_array():
    test_string = load_json_file('n_structure_unclosed_array.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_unclosed_array_partial_null():
    test_string = load_json_file('n_structure_unclosed_array_partial_null.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_unclosed_array_unfinished_false():
    test_string = load_json_file('n_structure_unclosed_array_unfinished_false.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_unclosed_array_unfinished_true():
    test_string = load_json_file('n_structure_unclosed_array_unfinished_true.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_unclosed_object():
    test_string = load_json_file('n_structure_unclosed_object.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_unicode_identifier():
    test_string = load_json_file('n_structure_unicode-identifier.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_UTF8_BOM_no_data():
    test_string = load_json_file('n_structure_UTF8_BOM_no_data.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_n_structure_whitespace_formfeed():
    test_string = load_json_file('n_structure_whitespace_formfeed.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_n_structure_whitespace_U+2060_word_joiner():
#     test_string = load_json_file('n_structure_whitespace_U+2060_word_joiner.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_arraysWithSpaces():
    test_string = load_json_file('y_array_arraysWithSpaces.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_empty_string():
    test_string = load_json_file('y_array_empty-string.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_empty():
    test_string = load_json_file('y_array_empty.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_ending_with_newline():
    test_string = load_json_file('y_array_ending_with_newline.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_false():
    test_string = load_json_file('y_array_false.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_heterogeneous():
    test_string = load_json_file('y_array_heterogeneous.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_null():
    test_string = load_json_file('y_array_null.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_with_1_and_newline():
    test_string = load_json_file('y_array_with_1_and_newline.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_with_leading_space():
    test_string = load_json_file('y_array_with_leading_space.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_with_several_null():
    test_string = load_json_file('y_array_with_several_null.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_array_with_trailing_space():
    test_string = load_json_file('y_array_with_trailing_space.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number():
    test_string = load_json_file('y_number.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    
#
# def test_y_number_0e+1():
#     test_string = load_json_file('y_number_0e+1.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#

def test_y_number_0e1():
    test_string = load_json_file('y_number_0e1.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_after_space():
    test_string = load_json_file('y_number_after_space.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_double_close_to_zero():
    test_string = load_json_file('y_number_double_close_to_zero.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_int_with_exp():
    test_string = load_json_file('y_number_int_with_exp.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_minus_zero():
    test_string = load_json_file('y_number_minus_zero.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_negative_int():
    test_string = load_json_file('y_number_negative_int.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_negative_one():
    test_string = load_json_file('y_number_negative_one.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_negative_zero():
    test_string = load_json_file('y_number_negative_zero.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_real_capital_e():
    test_string = load_json_file('y_number_real_capital_e.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_real_capital_e_neg_exp():
    test_string = load_json_file('y_number_real_capital_e_neg_exp.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_real_capital_e_pos_exp():
    test_string = load_json_file('y_number_real_capital_e_pos_exp.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_real_exponent():
    test_string = load_json_file('y_number_real_exponent.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_real_fraction_exponent():
    test_string = load_json_file('y_number_real_fraction_exponent.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_real_neg_exp():
    test_string = load_json_file('y_number_real_neg_exp.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_real_pos_exponent():
    test_string = load_json_file('y_number_real_pos_exponent.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_simple_int():
    test_string = load_json_file('y_number_simple_int.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_number_simple_real():
    test_string = load_json_file('y_number_simple_real.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object():
    test_string = load_json_file('y_object.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_basic():
    test_string = load_json_file('y_object_basic.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_duplicated_key():
    test_string = load_json_file('y_object_duplicated_key.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_duplicated_key_and_value():
    test_string = load_json_file('y_object_duplicated_key_and_value.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_empty():
    test_string = load_json_file('y_object_empty.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_empty_key():
    test_string = load_json_file('y_object_empty_key.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_escaped_null_in_key():
    test_string = load_json_file('y_object_escaped_null_in_key.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_extreme_numbers():
    test_string = load_json_file('y_object_extreme_numbers.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_long_strings():
    test_string = load_json_file('y_object_long_strings.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_simple():
    test_string = load_json_file('y_object_simple.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_string_unicode():
    test_string = load_json_file('y_object_string_unicode.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_object_with_newlines():
    test_string = load_json_file('y_object_with_newlines.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_1_2_3_bytes_UTF_8_sequences():
    test_string = load_json_file('y_string_1_2_3_bytes_UTF-8_sequences.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_accepted_surrogate_pair():
    test_string = load_json_file('y_string_accepted_surrogate_pair.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_accepted_surrogate_pairs():
    test_string = load_json_file('y_string_accepted_surrogate_pairs.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_allowed_escapes():
    test_string = load_json_file('y_string_allowed_escapes.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_backslash_and_u_escaped_zero():
    test_string = load_json_file('y_string_backslash_and_u_escaped_zero.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_backslash_doublequotes():
    test_string = load_json_file('y_string_backslash_doublequotes.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_comments():
    test_string = load_json_file('y_string_comments.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_double_escape_a():
    test_string = load_json_file('y_string_double_escape_a.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_double_escape_n():
    test_string = load_json_file('y_string_double_escape_n.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_escaped_control_character():
    test_string = load_json_file('y_string_escaped_control_character.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_escaped_noncharacter():
    test_string = load_json_file('y_string_escaped_noncharacter.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_in_array():
    test_string = load_json_file('y_string_in_array.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_in_array_with_leading_space():
    test_string = load_json_file('y_string_in_array_with_leading_space.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_last_surrogates_1_and_2():
    test_string = load_json_file('y_string_last_surrogates_1_and_2.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_nbsp_uescaped():
    test_string = load_json_file('y_string_nbsp_uescaped.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_y_string_nonCharacterInUTF_8_U+10FFFF():
#     test_string = load_json_file('y_string_nonCharacterInUTF-8_U+10FFFF.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_y_string_nonCharacterInUTF_8_U+FFFF():
#     test_string = load_json_file('y_string_nonCharacterInUTF-8_U+FFFF.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_null_escape():
    test_string = load_json_file('y_string_null_escape.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_one_byte_utf_8():
    test_string = load_json_file('y_string_one-byte-utf-8.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_pi():
    test_string = load_json_file('y_string_pi.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_y_string_reservedCharacterInUTF_8_U+1BFFF():
#     test_string = load_json_file('y_string_reservedCharacterInUTF-8_U+1BFFF.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#

def test_y_string_simple_ascii():
    test_string = load_json_file('y_string_simple_ascii.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_space():
    test_string = load_json_file('y_string_space.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

# def test_y_string_surrogates_U+1D11E_MUSICAL_SYMBOL_G_CLEF():
#     test_string = load_json_file('y_string_surrogates_U+1D11E_MUSICAL_SYMBOL_G_CLEF.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
def test_y_string_three_byte_utf_8():
    test_string = load_json_file('y_string_three-byte-utf-8.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_two_byte_utf_8():
    test_string = load_json_file('y_string_two-byte-utf-8.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    
#
# def test_y_string_u+2028_line_sep():
#     test_string = load_json_file('y_string_u+2028_line_sep.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_y_string_u+2029_par_sep():
#     test_string = load_json_file('y_string_u+2029_par_sep.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_uEscape():
    test_string = load_json_file('y_string_uEscape.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_uescaped_newline():
    test_string = load_json_file('y_string_uescaped_newline.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_unescaped_char_delete():
    test_string = load_json_file('y_string_unescaped_char_delete.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_unicode():
    test_string = load_json_file('y_string_unicode.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_unicodeEscapedBackslash():
    test_string = load_json_file('y_string_unicodeEscapedBackslash.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_unicode_2():
    test_string = load_json_file('y_string_unicode_2.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_unicode_escaped_double_quote():
    test_string = load_json_file('y_string_unicode_escaped_double_quote.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    
#
# def test_y_string_unicode_U+10FFFE_nonchar():
#     test_string = load_json_file('y_string_unicode_U+10FFFE_nonchar.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_y_string_unicode_U+1FFFE_nonchar():
#     test_string = load_json_file('y_string_unicode_U+1FFFE_nonchar.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_y_string_unicode_U+200B_ZERO_WIDTH_SPACE():
#     test_string = load_json_file('y_string_unicode_U+200B_ZERO_WIDTH_SPACE.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_y_string_unicode_U+2064_invisible_plus():
#     test_string = load_json_file('y_string_unicode_U+2064_invisible_plus.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_y_string_unicode_U+FDD0_nonchar():
#     test_string = load_json_file('y_string_unicode_U+FDD0_nonchar.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
# def test_y_string_unicode_U+FFFE_nonchar():
#     test_string = load_json_file('y_string_unicode_U+FFFE_nonchar.json')
#     assert fredson_parse(test_string) == json.loads(test_string)
#
#
def test_y_string_utf8():
    test_string = load_json_file('y_string_utf8.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_string_with_del_character():
    test_string = load_json_file('y_string_with_del_character.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_lonely_false():
    test_string = load_json_file('y_structure_lonely_false.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_lonely_int():
    test_string = load_json_file('y_structure_lonely_int.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_lonely_negative_real():
    test_string = load_json_file('y_structure_lonely_negative_real.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_lonely_null():
    test_string = load_json_file('y_structure_lonely_null.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_lonely_string():
    test_string = load_json_file('y_structure_lonely_string.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_lonely_true():
    test_string = load_json_file('y_structure_lonely_true.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_string_empty():
    test_string = load_json_file('y_structure_string_empty.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_trailing_newline():
    test_string = load_json_file('y_structure_trailing_newline.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_true_in_array():
    test_string = load_json_file('y_structure_true_in_array.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    

def test_y_structure_whitespace_array():
    test_string = load_json_file('y_structure_whitespace_array.json')
    assert fredson_parse(test_string) == json.loads(test_string)
    
