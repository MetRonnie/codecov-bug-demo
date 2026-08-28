import pytest

from main import greater_than_five, less_than_ten, is_zero


@pytest.mark.parametrize('input, expected', [
    (6, True),
    (5, False),
])
def test_greater_than_five(input, expected):
    assert greater_than_five(input) == expected


@pytest.mark.parametrize('input, expected', [
    (9, True),
    (10, False),
])
def test_less_than_ten(input, expected):
    assert less_than_ten(input) == expected


def test_is_zero():
    assert is_zero(0) is True
    assert is_zero(1) is False
