import pytest
from datetime import date
from datetime import timedelta

from tdd_tutorial.main import is_current, main

TODAY = date.today()
BEGIN_DATE = TODAY - timedelta(days=14)
END_DATE = TODAY + timedelta(days=14)
EXAMPLE_DCT = {
    'random_key': 'random_value',
    'begin_year': BEGIN_DATE.year,
    'begin_month': BEGIN_DATE.month,
    'begin_day': BEGIN_DATE.day,
    'end_year': END_DATE.year,
    'end_month': END_DATE.month,
    'end_day': END_DATE.day
}


@pytest.mark.parametrize(
    'test_case,expect',
    [(EXAMPLE_DCT, True)]
)
def test_is_current(test_case, expect):
    assert is_current(test_case) == expect


def test_main(example_yaml):
    assert main(example_yaml, today=date(1900, 1, 1)) == {
        'five': '==unknown==',
        'four': '==unknown==',
        'one': False,
        'seven': '==unknown==',
        'six': '==unknown==',
        'three': False,
        'two': False
    }
