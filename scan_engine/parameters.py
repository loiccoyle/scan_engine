'''Contains the two parameter types, Zipable and Productable.
'''
from itertools import product


class CombinationOutput(tuple):
    '''Helper class to distinguish combination output tuples from user set tuples.
    '''


class Parameter(list):
    """Parameter base class.
    """
    def __init__(self, *args):
        """Parameter base class, mainly used for type identification.

        Args:
            *args: elements to be contained in this Parameter instance.
        """
        super().__init__(args)

    def __radd__(self, other):
        """Forward __radd__ to __add__.
        """
        return self.__add__(other)


class Productable(Parameter):
    """This class handles the parameters which should follow the product rule.
    """
    def __add__(self, other):
        """Defines the combination behaviour. Creates the itertools.product of
        self and other.

        Args:
            other: the other object whith which to combine.

        Returns:
            Zipable: Zipable containing the result of the product.
        """
        if not other:
            return self
        if not isinstance(other, Parameter):
            other = _default_behaviour(other)

        return Zipable(*(CombinationOutput(i) for i in product(self, other)))

    def __repr__(self):
        return f'P({super().__repr__()[1:-1]})'


class Zipable(Parameter):
    """This class handles the parameters which should follow the zip rule.
    """
    def __add__(self, other):
        """Defines the combination behaviour. Creates the zip of self and other.

        Args:
            other: the other object whith which to combine.

        Returns:
            Zipable: Zipable containing the result of the zip.
        """
        if not other:
            return self
        if not isinstance(other, (Productable, Zipable)):
            other = _default_behaviour(other)

        if isinstance(other, Productable):
            return Zipable(*(CombinationOutput(i) for i in product(self, other)))

        return Zipable(*(CombinationOutput(i) for i in zip(self, other)))

    def __repr__(self):
        return f'Z({super().__repr__()[1:-1]})'


def _default_behaviour(other):
    return Productable(other)
