import enum


class Method(enum.Enum):
    GOLD_SLICE = 0
    CHORDS = 1
    NEWTON_RAFSON = 2
    CHORDS_AND_NEWTON_RAFSON = 3
    PARALLEL_GOLD_SLICE_AND_CHORDS_AND_NEWTON_RAFSON = 4

    def translate(self):
        match self:
            case Method.GOLD_SLICE:
                return 'Золотого сечения'
            case Method.CHORDS:
                return 'Хорд'
            case Method.NEWTON_RAFSON:
                return 'Ньютона-Рафсона'
            case Method.CHORDS_AND_NEWTON_RAFSON:
                return 'Комбинированный (хорд и Ньютона-Рафсона)'
            case Method.PARALLEL_GOLD_SLICE_AND_CHORDS_AND_NEWTON_RAFSON:
                return 'Параллельный (зол. сечения и комбинированного)'
