import random
from dataclasses import dataclass


@dataclass
class Place:
    name: str
    url: str


class PlacesDal:

    PLACES_LIST = [
        Place("Shavi lomi", "https://maps.app.goo.gl/GEPzdGHhzezCMdRP8"),
        Place("Shemomechama", "https://maps.app.goo.gl/8ZeversGnFDcMQ98A"),
        Place("Klike", "https://maps.app.goo.gl/3fUubLFDuuyQhCWZ9"),
        Place("Culinarium Khasheria", "https://maps.app.goo.gl/vfo8WzcTvYTcDryZ8"),
        Place(
            "Marani Restaurant & Bar",
            "https://maps.google.com/?cid=12699934122655675480",
        ),
        Place("KAKHELEBI", "https://goo.gl/maps/iuvMfwHAD9EmYMu76"),
        Place("MartoKhinkali", "https://maps.app.goo.gl/RkGBf9LjR7knioXn6"),
        Place("Manji", "https://goo.gl/maps/r5TszwT8RD565gbWA"),
    ]

    def fetch_random(self) -> Place:
        return random.choice(self.PLACES_LIST)
