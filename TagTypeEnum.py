from enum import Enum
import json


class TagType(Enum):
    TEMPERATURE = 1,
    RHT = 2,
    DISTANCE = 3,
    ANG = 4,
    OTHER = 5
