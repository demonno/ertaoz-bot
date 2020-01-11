from datetime import date, datetime
from typing import List, Iterable

import pytz


class TripNotFoundError(Exception):
    pass


class TripsDal:
    OUTBOUND_TRIPS = {
        1: date(day=11, month=12, year=2019),
        2: date(day=15, month=12, year=2019),
        3: date(day=15, month=12, year=2019),
        4: date(day=18, month=12, year=2019),
        5: date(day=18, month=12, year=2019),
        6: date(day=22, month=12, year=2019),
        7: date(day=22, month=12, year=2019),
        8: date(day=22, month=12, year=2019),
        9: date(day=22, month=12, year=2019),
        10: date(day=22, month=12, year=2019),
        11: date(day=22, month=12, year=2019),
        12: date(day=22, month=12, year=2019),
        13: date(day=22, month=12, year=2019),
    }

    INBOUND_TRIPS = {
        1: date(day=5, month=1, year=2020),
        2: date(day=9, month=1, year=2020),
        3: date(day=5, month=1, year=2020),
        4: date(day=4, month=1, year=2020),
        5: date(day=4, month=1, year=2020),
        6: date(day=5, month=1, year=2020),
        7: date(day=5, month=1, year=2020),
        8: date(day=5, month=1, year=2020),
        9: date(day=5, month=1, year=2020),
        10: date(day=12, month=1, year=2020),
        11: date(day=29, month=1, year=2020),
        12: date(day=12, month=1, year=2020),
        13: date(day=19, month=1, year=2020),
    }

    def fetch_outbound_trip(self, user_id):
        try:
            return self.OUTBOUND_TRIPS[user_id]
        except KeyError:
            raise TripNotFoundError(f"Outbound trip not found for user <{user_id}>")

    def fetch_inbound_trip(self, user_id):
        try:
            return self.INBOUND_TRIPS[user_id]
        except KeyError:
            raise TripNotFoundError(f"Inbound trip not found for user <{user_id}>")

    @property
    def users_leaving_today(self) -> Iterable[int]:
        today = datetime.now(tz=pytz.timezone("Europe/Tallinn"))

        trips = {
            user_id: departure for user_id, departure in self.OUTBOUND_TRIPS.items() if today.day - departure.day == 0
        }

        yield from trips.keys()

    @property
    def users_leaving_tomorrow(self) -> List[int]:
        today = datetime.now(tz=pytz.timezone("Europe/Tallinn"))

        trips = {
            user_id: departure for user_id, departure in self.OUTBOUND_TRIPS.items() if today.day - departure.day == 1
        }

        yield from trips.keys()
