import enum

from algorithms.chords import *
from algorithms.gold_slice import *
from algorithms.newton_rafson import *

class Method(enum.Enum):
    GOLD_SLICE = 0
    CHORDS = 1
    NEWTON_RAFSON = 2