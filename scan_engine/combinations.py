'''Contains the two parameter types, Zipable and Productable.
'''
from itertools import product


class CombinationOutput(tuple):
    '''Helper class to distinguish combination output tuples from user set tuples.
    '''


class Combination(list):
    """Combination base class.
    """
    def __init__(self, *args):
        """Combination base class, mainly used for type identification.

        Args:
            *args: elements to be contained in this Combination instance.
        """
        super().__init__(args)

    @staticmethod
    def _combine(this, that):
        pass

    def __add__(self, other):
        """Forward __radd__ to __add__.
        """
        if not other:
            return self
        return self._combine(self, other)

    def __radd__(self, other):
        """Forward __radd__ to __add__.
        """
        if not other:
            return self
        return self._combine(other, self)


class Productable(Combination):
    """This class handles the parameters which should follow the product rule.
    """
    @staticmethod
    def _combine(this, that):
        """Defines the combination behaviour. Creates the itertools.product of
        this and that.

        Args:
            that: the object whith which to combine.

        Returns:
            Zipable: Zipable containing the result of the product.
        """
        if not isinstance(that, Combination):
            that = _default_behaviour(that)
        if not isinstance(this, Combination):
            this = _default_behaviour(this)

        return Zipable(*(CombinationOutput(i) for i in product(this, that)))


class Zipable(Combination):
    """This class handles the parameters which should follow the zip rule.
    """
    @staticmethod
    def _combine(this, that):
        """Defines the combination behaviour. Creates the zip of this and that.

        Args:
            that: the object whith which to combine.

        Returns:
            Zipable: Zipable containing the result of the zip.
        """
        if not isinstance(that, (Productable, Zipable)):
            that = _default_behaviour(that)
        if not isinstance(this, (Productable, Zipable)):
            this = _default_behaviour(this)

        if isinstance(that, Productable):
            return Zipable(*(CombinationOutput(i) for i in product(this, that)))

        return Zipable(*(CombinationOutput(i) for i in zip(this, that)))

    def __repr__(self):
        return f'Z({super().__repr__()[1:-1]})'


def _default_behaviour(other):
    if isinstance(other, list):
        out = Productable(*other)
    else:
        out = Productable(other)
    return out
