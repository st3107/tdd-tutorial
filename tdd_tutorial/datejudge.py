from datetime import datetime


def read(file: str) -> dict:
    dct = dict()
    return dct


def get_events(dct: dict) -> list:
    events = []
    return events


def is_current(dct: dict) -> bool:
    flag = False
    begin_date = datetime(dct['begin_year'], dct['begin_month'], dct['begin_day'])
    end_date = datetime(dct['end_year'], dct['end_month'], dct['end_day'])
    today = datetime.today()
    if begin_date <= today < end_date:
        flag = True
    return flag


def printout(flag: bool):
    return
