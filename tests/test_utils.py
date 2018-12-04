from _utils import noun_number


def test_given_one_should_return_empty_suffix():
    assert noun_number(1) == ''


def test_given_zero_should_return_s():
    assert noun_number(0) == 's'


def test_given_more_than_one_should_return_s():
    assert noun_number(100) == 's'
