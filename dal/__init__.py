from dataclasses import dataclass, field

from dal.places_dal import PlacesDal
from dal.wisdom_dal import WisdomDal


@dataclass
class DataAccessLayer:
    places: PlacesDal = field(default_factory=PlacesDal)
    wisdoms: WisdomDal = field(default_factory=WisdomDal)
