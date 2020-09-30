from dataclasses import dataclass, field

from dal.places_dal import PlacesDal
from dal.trips_dal import TripsDal
from dal.wisdom_dal import WisdomDal


@dataclass
class DataAccessLayer:
    places: PlacesDal = field(default_factory=PlacesDal)
    wisdoms: WisdomDal = field(default_factory=WisdomDal)
    trips: TripsDal = field(default_factory=TripsDal)
