from datetime import date
from typing import Generator, Union, Dict
import yaml


def read(filename: str) -> dict:
    """Safe load the yaml file.

    Parameters
    ----------
    filename : str
        The path to the yaml file.

    Returns
    -------
    dct : dict
        The dictionary loaded from the yaml file.
    """
    with open(filename, "r") as f:
        dct = yaml.safe_load(f)
    return dct


def get_appointments(db: dict) -> Generator:
    """Get all the appointments record inside a database.

    Parameters
    ----------
    db : dict
        A dictionary that is a database for people's appointments.

    Yields
    ------
    key : str
        The key to the appointment.

    appointment : dict
        The record of the appointment.
    """
    for uid, doc in db.items():
        appointments = doc.get('appointments', {})
        for key, appointment in appointments.items():
            yield key, appointment


# this is the required fields for the dct in is_current
REQUID_FIELDS = (
    'begin_year',
    'begin_month',
    'begin_day',
    'end_year',
    'end_month',
    'end_day'
)


def is_current(dct: dict, today: date = None) -> Union[bool, str]:
    """Judge a record is a current record or not.

    Parameters
    ----------
    dct : dict
        A record with required fields in REQUID_FIELDS.

    today : date
        A argument for the today's date. If None, use the date that the function is called. It is for testing.

    Returns
    -------
    flag : bool or str
        If the record is current, return True. Otherwise, return False. If missing required fields, which means,
        not enough info to judge the date of begin and end, return "==unknown==".
    """
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
    """Read the record in a yaml file and return whether the appointments are current or not in a dictionary.

    It will return a dictionary that the key is the key of the appointments and the value is whether the
    appointment is current or not.If the record is current, return True. Otherwise, return False. If missing
    required fields, which means, not enough info to judge the date of begin and end, return "==unknown==".

    Parameters
    ----------
    filename : str
        The path to the yaml file.

    today : date
        A argument for the today's date. If None, use the date that the function is called. It is for testing.

    Returns
    -------
    is_current_dct : dict
        A dictionary that tells appointments are current or not.
    """
    db = read(filename)
    appointments = get_appointments(db)
    return {
        key: is_current(appointment, today=today)
        for key, appointment in appointments
    }
