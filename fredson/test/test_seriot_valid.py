import json
from fredson import fredson_parse


def load_json_file(filename, encoding="utf8"):
    with open('seriot_test_suite/' + filename, encoding=encoding) as f:
        input_string = f.read()
    return input_string


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


def test_y_number_0e_plus1():
    test_string = load_json_file('y_number_0e+1.json')
    assert fredson_parse(test_string) == json.loads(test_string)


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


def test_y_string_nonCharacterInUTF_8_U_plus10FFFF():
    test_string = load_json_file('y_string_nonCharacterInUTF-8_U+10FFFF.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_nonCharacterInUTF_8_U_plus_FFFF():
    test_string = load_json_file('y_string_nonCharacterInUTF-8_U+FFFF.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_null_escape():
    test_string = load_json_file('y_string_null_escape.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_one_byte_utf_8():
    test_string = load_json_file('y_string_one-byte-utf-8.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_pi():
    test_string = load_json_file('y_string_pi.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_reservedCharacterInUTF_8_U_plus_1BFFF():
    test_string = load_json_file('y_string_reservedCharacterInUTF-8_U+1BFFF.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_simple_ascii():
    test_string = load_json_file('y_string_simple_ascii.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_space():
    test_string = load_json_file('y_string_space.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_surrogates_U_plus1D11E_MUSICAL_SYMBOL_G_CLEF():
    test_string = load_json_file('y_string_surrogates_U+1D11E_MUSICAL_SYMBOL_G_CLEF.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_three_byte_utf_8():
    test_string = load_json_file('y_string_three-byte-utf-8.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_two_byte_utf_8():
    test_string = load_json_file('y_string_two-byte-utf-8.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_u_plus2028_line_sep():
    test_string = load_json_file('y_string_u+2028_line_sep.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_u_plus2029_par_sep():
    test_string = load_json_file('y_string_u+2029_par_sep.json')
    assert fredson_parse(test_string) == json.loads(test_string)


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


def test_y_string_unicode_U_plus10FFFE_nonchar():
    test_string = load_json_file('y_string_unicode_U+10FFFE_nonchar.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_unicode_U_plus1FFFE_nonchar():
    test_string = load_json_file('y_string_unicode_U+1FFFE_nonchar.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_unicode_U_plus200B_ZERO_WIDTH_SPACE():
    test_string = load_json_file('y_string_unicode_U+200B_ZERO_WIDTH_SPACE.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_unicode_Uplus2064_invisible_plus():
    test_string = load_json_file('y_string_unicode_U+2064_invisible_plus.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_unicode_UplusFDD0_nonchar():
    test_string = load_json_file('y_string_unicode_U+FDD0_nonchar.json')
    assert fredson_parse(test_string) == json.loads(test_string)


def test_y_string_unicode_UplusFFFE_nonchar():
    test_string = load_json_file('y_string_unicode_U+FFFE_nonchar.json')
    assert fredson_parse(test_string) == json.loads(test_string)


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

