import pytest

from fredson_exceptions import FredsonTokenError, FredsonParseError
from fredson import fredson_parse


def load_json_file(filename, encoding="utf8"):
    with open('seriot_test_suite/' + filename, encoding=encoding) as f:
        input_string = f.read()
    return input_string


def test_n_array_1_true_without_comma():
    test_string = load_json_file('n_array_1_true_without_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_a_invalid_utf8():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_array_a_invalid_utf8.json')


def test_n_array_colon_instead_of_comma():
    test_string = load_json_file('n_array_colon_instead_of_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_comma_after_close():
    test_string = load_json_file('n_array_comma_after_close.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_comma_and_number():
    test_string = load_json_file('n_array_comma_and_number.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_double_comma():
    test_string = load_json_file('n_array_double_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_double_extra_comma():
    test_string = load_json_file('n_array_double_extra_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_extra_close():
    test_string = load_json_file('n_array_extra_close.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_extra_comma():
    test_string = load_json_file('n_array_extra_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_incomplete():
    test_string = load_json_file('n_array_incomplete.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_incomplete_invalid_value():
    test_string = load_json_file('n_array_incomplete_invalid_value.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_array_inner_array_no_comma():
    test_string = load_json_file('n_array_inner_array_no_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_invalid_utf8():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_array_invalid_utf8.json')


def test_n_array_items_separated_by_semicolon():
    test_string = load_json_file('n_array_items_separated_by_semicolon.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_just_comma():
    test_string = load_json_file('n_array_just_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_just_minus():
    test_string = load_json_file('n_array_just_minus.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_array_missing_value():
    test_string = load_json_file('n_array_missing_value.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_newlines_unclosed():
    test_string = load_json_file('n_array_newlines_unclosed.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_number_and_comma():
    test_string = load_json_file('n_array_number_and_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_number_and_several_commas():
    test_string = load_json_file('n_array_number_and_several_commas.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_spaces_vertical_tab_formfeed():
    test_string = load_json_file('n_array_spaces_vertical_tab_formfeed.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_array_star_inside():
    test_string = load_json_file('n_array_star_inside.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_array_unclosed():
    test_string = load_json_file('n_array_unclosed.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_unclosed_trailing_comma():
    test_string = load_json_file('n_array_unclosed_trailing_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_unclosed_with_new_lines():
    test_string = load_json_file('n_array_unclosed_with_new_lines.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_array_unclosed_with_object_inside():
    test_string = load_json_file('n_array_unclosed_with_object_inside.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_incomplete_false():
    test_string = load_json_file('n_incomplete_false.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_incomplete_null():
    test_string = load_json_file('n_incomplete_null.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_incomplete_true():
    test_string = load_json_file('n_incomplete_true.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_multidigit_number_then_00():
    test_string = load_json_file('n_multidigit_number_then_00.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_plus():
    test_string = load_json_file('n_number_++.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_plus1():
    test_string = load_json_file('n_number_+1.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_plusInf():
    test_string = load_json_file('n_number_+Inf.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number__01():
    test_string = load_json_file('n_number_-01.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number__1_0_():
    test_string = load_json_file('n_number_-1.0..json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number__2_():
    test_string = load_json_file('n_number_-2..json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number__NaN():
    test_string = load_json_file('n_number_-NaN.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number___1():
    test_string = load_json_file('n_number_.-1.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number__2e_3():
    test_string = load_json_file('n_number_.2e-3.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_0_1_2():
    test_string = load_json_file('n_number_0.1.2.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_0_3eplus():
    test_string = load_json_file('n_number_0.3e+.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_0_3e():
    test_string = load_json_file('n_number_0.3e.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_0_e1():
    test_string = load_json_file('n_number_0.e1.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_0eplus():
    test_string = load_json_file('n_number_0e+.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_0e():
    test_string = load_json_file('n_number_0e.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_0_capital_Eplus():
    test_string = load_json_file('n_number_0_capital_E+.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_0_capital_E():
    test_string = load_json_file('n_number_0_capital_E.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_1_0eplus():
    test_string = load_json_file('n_number_1.0e+.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_1_0e_():
    test_string = load_json_file('n_number_1.0e-.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_1_0e():
    test_string = load_json_file('n_number_1.0e.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_1eE2():
    test_string = load_json_file('n_number_1eE2.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_1_000():
    test_string = load_json_file('n_number_1_000.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_2_eplus3():
    test_string = load_json_file('n_number_2.e+3.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_2_e_3():
    test_string = load_json_file('n_number_2.e-3.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_2_e3():
    test_string = load_json_file('n_number_2.e3.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_9_eplus():
    test_string = load_json_file('n_number_9.e+.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_expression():
    test_string = load_json_file('n_number_expression.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_hex_1_digit():
    test_string = load_json_file('n_number_hex_1_digit.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_hex_2_digits():
    test_string = load_json_file('n_number_hex_2_digits.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_Inf():
    test_string = load_json_file('n_number_Inf.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_infinity():
    test_string = load_json_file('n_number_infinity.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_invalidplus_():
    test_string = load_json_file('n_number_invalid+-.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_invalid_negative_real():
    test_string = load_json_file('n_number_invalid-negative-real.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_invalid_utf_8_in_bigger_int():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_number_invalid-utf-8-in-bigger-int.json')


def test_n_number_invalid_utf_8_in_exponent():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_number_invalid-utf-8-in-exponent.json')


def test_n_number_invalid_utf_8_in_int():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_number_invalid-utf-8-in-int.json')


def test_n_number_minus_infinity():
    with pytest.raises(FredsonTokenError):
        test_string = load_json_file('n_number_minus_infinity.json')
        fredson_parse(test_string)


def test_n_number_minus_sign_with_trailing_garbage():
    with pytest.raises(FredsonTokenError):
        test_string = load_json_file('n_number_minus_sign_with_trailing_garbage.json')
        fredson_parse(test_string)


def test_n_number_minus_space_1():
    test_string = load_json_file('n_number_minus_space_1.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_NaN():
    test_string = load_json_file('n_number_NaN.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_neg_int_starting_with_zero():
    test_string = load_json_file('n_number_neg_int_starting_with_zero.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_neg_real_without_int_part():
    test_string = load_json_file('n_number_neg_real_without_int_part.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_neg_with_garbage_at_end():
    test_string = load_json_file('n_number_neg_with_garbage_at_end.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_real_garbage_after_e():
    test_string = load_json_file('n_number_real_garbage_after_e.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_real_without_fractional_part():
    test_string = load_json_file('n_number_real_without_fractional_part.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_real_with_invalid_utf8_after_e():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_number_real_with_invalid_utf8_after_e.json')


def test_n_number_starting_with_dot():
    test_string = load_json_file('n_number_starting_with_dot.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_number_UplusFF11_fullwidth_digit_one():
    test_string = load_json_file('n_number_U+FF11_fullwidth_digit_one.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_with_alpha():
    test_string = load_json_file('n_number_with_alpha.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_with_alpha_char():
    test_string = load_json_file('n_number_with_alpha_char.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_number_with_leading_zero():
    test_string = load_json_file('n_number_with_leading_zero.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_bad_value():
    test_string = load_json_file('n_object_bad_value.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_bracket_key():
    test_string = load_json_file('n_object_bracket_key.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_comma_instead_of_colon():
    test_string = load_json_file('n_object_comma_instead_of_colon.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_double_colon():
    test_string = load_json_file('n_object_double_colon.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_emoji():
    test_string = load_json_file('n_object_emoji.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_garbage_at_end():
    test_string = load_json_file('n_object_garbage_at_end.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_key_with_single_quotes():
    test_string = load_json_file('n_object_key_with_single_quotes.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_lone_continuation_byte_in_key_and_trailing_comma():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_object_lone_continuation_byte_in_key_and_trailing_comma.json')


def test_n_object_missing_colon():
    test_string = load_json_file('n_object_missing_colon.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_missing_key():
    test_string = load_json_file('n_object_missing_key.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_missing_semicolon():
    test_string = load_json_file('n_object_missing_semicolon.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_missing_value():
    test_string = load_json_file('n_object_missing_value.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_no_colon():
    test_string = load_json_file('n_object_no-colon.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_non_string_key():
    test_string = load_json_file('n_object_non_string_key.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_non_string_key_but_huge_number_instead():
    test_string = load_json_file('n_object_non_string_key_but_huge_number_instead.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_repeated_null_null():
    test_string = load_json_file('n_object_repeated_null_null.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_several_trailing_commas():
    test_string = load_json_file('n_object_several_trailing_commas.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_single_quote():
    test_string = load_json_file('n_object_single_quote.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_trailing_comma():
    test_string = load_json_file('n_object_trailing_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_trailing_comment():
    test_string = load_json_file('n_object_trailing_comment.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_trailing_comment_open():
    test_string = load_json_file('n_object_trailing_comment_open.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_trailing_comment_slash_open():
    test_string = load_json_file('n_object_trailing_comment_slash_open.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_trailing_comment_slash_open_incomplete():
    test_string = load_json_file('n_object_trailing_comment_slash_open_incomplete.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_two_commas_in_a_row():
    test_string = load_json_file('n_object_two_commas_in_a_row.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_unquoted_key():
    test_string = load_json_file('n_object_unquoted_key.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_unterminated_value():
    test_string = load_json_file('n_object_unterminated-value.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_object_with_single_string():
    test_string = load_json_file('n_object_with_single_string.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_object_with_trailing_garbage():
    test_string = load_json_file('n_object_with_trailing_garbage.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_single_space():
    test_string = load_json_file('n_single_space.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_string_1_surrogate_then_escape():
    test_string = load_json_file('n_string_1_surrogate_then_escape.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_1_surrogate_then_escape_u():
    test_string = load_json_file('n_string_1_surrogate_then_escape_u.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_1_surrogate_then_escape_u1():
    test_string = load_json_file('n_string_1_surrogate_then_escape_u1.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_1_surrogate_then_escape_u1x():
    test_string = load_json_file('n_string_1_surrogate_then_escape_u1x.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_accentuated_char_no_quotes():
    test_string = load_json_file('n_string_accentuated_char_no_quotes.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_backslash_00():
    test_string = load_json_file('n_string_backslash_00.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_escaped_backslash_bad():
    test_string = load_json_file('n_string_escaped_backslash_bad.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_escaped_ctrl_char_tab():
    test_string = load_json_file('n_string_escaped_ctrl_char_tab.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_escaped_emoji():
    test_string = load_json_file('n_string_escaped_emoji.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_escape_x():
    test_string = load_json_file('n_string_escape_x.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_incomplete_escape():
    test_string = load_json_file('n_string_incomplete_escape.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_incomplete_escaped_character():
    test_string = load_json_file('n_string_incomplete_escaped_character.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_incomplete_surrogate():
    test_string = load_json_file('n_string_incomplete_surrogate.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_incomplete_surrogate_escape_invalid():
    test_string = load_json_file('n_string_incomplete_surrogate_escape_invalid.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_invalid_utf_8_in_escape():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_string_invalid-utf-8-in-escape.json')


def test_n_string_invalid_backslash_esc():
    test_string = load_json_file('n_string_invalid_backslash_esc.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_invalid_unicode_escape():
    test_string = load_json_file('n_string_invalid_unicode_escape.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_invalid_utf8_after_escape():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_string_invalid_utf8_after_escape.json')


def test_n_string_leading_uescaped_thinspace():
    test_string = load_json_file('n_string_leading_uescaped_thinspace.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_no_quotes_with_bad_escape():
    test_string = load_json_file('n_string_no_quotes_with_bad_escape.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_single_doublequote():
    test_string = load_json_file('n_string_single_doublequote.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_single_quote():
    test_string = load_json_file('n_string_single_quote.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_single_string_no_double_quotes():
    test_string = load_json_file('n_string_single_string_no_double_quotes.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_start_escape_unclosed():
    test_string = load_json_file('n_string_start_escape_unclosed.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_unescaped_ctrl_char():
    test_string = load_json_file('n_string_unescaped_ctrl_char.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_unescaped_newline():
    test_string = load_json_file('n_string_unescaped_newline.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_unescaped_tab():
    test_string = load_json_file('n_string_unescaped_tab.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_unicode_CapitalU():
    test_string = load_json_file('n_string_unicode_CapitalU.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_string_with_trailing_garbage():
    test_string = load_json_file('n_string_with_trailing_garbage.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_100000_opening_arrays():
    test_string = load_json_file('n_structure_100000_opening_arrays.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_angle_bracket__():
    test_string = load_json_file('n_structure_angle_bracket_..json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_angle_bracket_null():
    test_string = load_json_file('n_structure_angle_bracket_null.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_array_trailing_garbage():
    test_string = load_json_file('n_structure_array_trailing_garbage.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_array_with_extra_array_close():
    test_string = load_json_file('n_structure_array_with_extra_array_close.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_array_with_unclosed_string():
    test_string = load_json_file('n_structure_array_with_unclosed_string.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_ascii_unicode_identifier():
    test_string = load_json_file('n_structure_ascii-unicode-identifier.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_capitalized_True():
    test_string = load_json_file('n_structure_capitalized_True.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_close_unopened_array():
    test_string = load_json_file('n_structure_close_unopened_array.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_comma_instead_of_closing_brace():
    test_string = load_json_file('n_structure_comma_instead_of_closing_brace.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_double_array():
    test_string = load_json_file('n_structure_double_array.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_end_array():
    test_string = load_json_file('n_structure_end_array.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_incomplete_UTF8_BOM():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_structure_incomplete_UTF8_BOM.json')


def test_n_structure_lone_invalid_utf_8():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_structure_lone-invalid-utf-8.json')


def test_n_structure_lone_open_bracket():
    test_string = load_json_file('n_structure_lone-open-bracket.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_no_data():
    test_string = load_json_file('n_structure_no_data.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_null_byte_outside_string():
    test_string = load_json_file('n_structure_null-byte-outside-string.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_number_with_trailing_garbage():
    test_string = load_json_file('n_structure_number_with_trailing_garbage.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_object_followed_by_closing_object():
    test_string = load_json_file('n_structure_object_followed_by_closing_object.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_object_unclosed_no_value():
    test_string = load_json_file('n_structure_object_unclosed_no_value.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_object_with_comment():
    test_string = load_json_file('n_structure_object_with_comment.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_object_with_trailing_garbage():
    test_string = load_json_file('n_structure_object_with_trailing_garbage.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_open_array_apostrophe():
    test_string = load_json_file('n_structure_open_array_apostrophe.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_open_array_comma():
    test_string = load_json_file('n_structure_open_array_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_open_array_object():
    test_string = load_json_file('n_structure_open_array_object.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_open_array_open_object():
    test_string = load_json_file('n_structure_open_array_open_object.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_open_array_open_string():
    test_string = load_json_file('n_structure_open_array_open_string.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_open_array_string():
    test_string = load_json_file('n_structure_open_array_string.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_open_object():
    test_string = load_json_file('n_structure_open_object.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_open_object_close_array():
    test_string = load_json_file('n_structure_open_object_close_array.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_open_object_comma():
    test_string = load_json_file('n_structure_open_object_comma.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_open_object_open_array():
    test_string = load_json_file('n_structure_open_object_open_array.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_open_object_open_string():
    test_string = load_json_file('n_structure_open_object_open_string.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_open_object_string_with_apostrophes():
    test_string = load_json_file('n_structure_open_object_string_with_apostrophes.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_open_open():
    test_string = load_json_file('n_structure_open_open.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_single_eacute():
    with pytest.raises(UnicodeDecodeError):
        test_string = load_json_file('n_structure_single_eacute.json')


def test_n_structure_single_star():
    test_string = load_json_file('n_structure_single_star.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_trailing_hash():
    test_string = load_json_file('n_structure_trailing_#.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_Uplus2060_word_joined():
    test_string = load_json_file('n_structure_U+2060_word_joined.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_uescaped_LF_before_string():
    test_string = load_json_file('n_structure_uescaped_LF_before_string.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_unclosed_array():
    test_string = load_json_file('n_structure_unclosed_array.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_unclosed_array_partial_null():
    test_string = load_json_file('n_structure_unclosed_array_partial_null.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_unclosed_array_unfinished_false():
    test_string = load_json_file('n_structure_unclosed_array_unfinished_false.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_unclosed_array_unfinished_true():
    test_string = load_json_file('n_structure_unclosed_array_unfinished_true.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_unclosed_object():
    test_string = load_json_file('n_structure_unclosed_object.json')
    with pytest.raises(FredsonParseError):
        fredson_parse(test_string)


def test_n_structure_unicode_identifier():
    test_string = load_json_file('n_structure_unicode-identifier.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_UTF8_BOM_no_data():
    test_string = load_json_file('n_structure_UTF8_BOM_no_data.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_whitespace_formfeed():
    test_string = load_json_file('n_structure_whitespace_formfeed.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)


def test_n_structure_whitespace_Uplus2060_word_joiner():
    test_string = load_json_file('n_structure_whitespace_U+2060_word_joiner.json')
    with pytest.raises(FredsonTokenError):
        fredson_parse(test_string)
