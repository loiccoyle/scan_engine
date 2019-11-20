from itertools import product


class Params(list):
    def __init__(self, *args):
        super().__init__(args)

    def __radd__(self, other):
        return self.__add__(other)


class Productable(Params):
    def __add__(self, other):
        if not other:
            return self
        if not isinstance(other, Params):
            other = _default_behaviour(other)

        return Zipable(*product(self, other))

    def __repr__(self):
        return f'P({super().__repr__()[1:-1]})'


class Zipable(Params):
    def __add__(self, other):
        if not other:
            return self
        if not isinstance(other, (Productable, Zipable)):
            other = _default_behaviour(other)

        if isinstance(other, Productable):
            return Zipable(*product(self, other))
        else:
            return Zipable(*zip(self, other))

    def __repr__(self):
        return f'Z({super().__repr__()[1:-1]})'


def _default_behaviour(other):
    return Productable(other)
