
class Weights:
    DEFAULT = 1


class Key(object):
    def __init__(self, key, weight=Weights.DEFAULT):
        self._key = key
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    @property
    def key(self):
        return self._key
    
    def __repr__(self) -> str:
        return f"<Key (weight={self._weight})"