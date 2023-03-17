import numberstrings_kata as nsk


def test_no_sum():
    assert nsk.sum_strings('', '') == '0'


def test_0digit_sum():
    assert nsk.sum_strings('12', '') == '12'


def test_1digit_sum():
    assert nsk.sum_strings('1', '1') == '2'


def test_1digit_sum_over10():
    assert nsk.sum_strings('7', '7') == '14'


def test_2digit_sum():
    assert nsk.sum_strings('12', '13') == '25'


def test_2digit_sum_over10():
    assert nsk.sum_strings('17', '27') == '44'


def test_bigint_sum():
    assert nsk.sum_strings('9223372036854775807', '13') == '9223372036854775820'


def test_2bigint_sum():
    assert nsk.sum_strings('9223372036854775807', '9223372036854775807') == '18446744073709551614'


def test_very_bigint_sum():
    assert nsk.sum_strings('111111111111111111111111111111',
                           '111111111111111111111111111111') == '222222222222222222222222222222'

