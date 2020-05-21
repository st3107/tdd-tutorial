from datetime import date
from typing import Generator, Union, Dict
import yaml


def read(filename: str) -> dict:
    with open(filename, "r") as f:
        dct = yaml.safe_load(f)
    return dct


def get_appointments(db: dict) -> Generator:
    for uid, doc in db.items():
        appointments = doc.get('appointments', {})
        for key, appointment in appointments.items():
            yield key, appointment


REQUID_FIELDS = (
    'begin_year',
    'begin_month',
    'begin_day',
    'end_year',
    'end_month',
    'end_day'
)


def is_current(dct: dict, today: date = None) -> Union[bool, str]:
    if today is None:
        today = date.today()
    for field in REQUID_FIELDS:
        if field not in dct:
            return "==unknown=="
    flag = False
    begin_date = date(dct['begin_year'], dct['begin_month'], dct['begin_day'])
    end_date = date(dct['end_year'], dct['end_month'], dct['end_day'])
    if begin_date <= today < end_date:
        flag = True
    return flag


def main(filename: str, today: date = None) -> Dict[str, bool]:
    db = read(filename)
    appointments = get_appointments(db)
    return {
        key: is_current(appointment, today=today)
        for key, appointment in appointments
    }
