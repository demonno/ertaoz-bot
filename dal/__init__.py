from dataclasses import dataclass, field

from dal.wisdom_dal import WisdomDal


@dataclass
class DataAccessLayer:
    wisdoms: WisdomDal = field(default_factory=WisdomDal)
