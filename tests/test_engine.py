"""engine.py unit tests.
"""
import unittest
from itertools import product
from scan_engine import Productable as P
from scan_engine import Zipable as Z
from scan_engine import engine

from scan_engine.engine import flatten
from scan_engine.engine import grouper


class TestEngineZipable(unittest.TestCase):
    """Test behaviour of the engine with Zipables.
    """
    def test_engine_zipable_zipable(self):
        """Tests the behaviour of the engine on non nested Zipables.
        """
        var1 = Z(1, 2, 3)
        var2 = Z(4, 5, 6)
        var3 = Z(7, 8, 9)
        var4 = Z(10, 11, 12)
        self.assertEqual(list(engine(var1, var2, var3, var4)),
                         list(grouper(flatten(var1 + var2 + var3 + var4), 4)))

    def test_engine_nested_zipable(self):
        """Tests the behaviour of the engine on nested Zipables.
        """
        var1 = Z(Z(1, 2, 3), Z(4, 5, 6))
        var2 = Z(Z(7, 8, 9), Z(10, 11, 12))
        self.assertEqual(list(engine(var1, var2)),
                         Z(*zip([1, 2, 3, 4, 5, 6],
                                [7, 8, 9, 10, 11, 12])))

    def test_engine_nested_zipable_3(self):
        """Tests the behaviour of the engine on 3 nested Zipables.
        """
        var1 = Z(Z(1, 2, 3), Z(4, 5, 6))
        var2 = Z(Z(7, 8, 9), Z(10, 11, 12))
        var3 = Z(Z(13, 14, 15), Z(16, 17, 18))
        res = zip([1, 2, 3, 4, 5, 6],
                  [7, 8, 9, 10, 11, 12],
                  [13, 14, 15, 16, 17, 18])
        self.assertEqual(list(engine(var1, var2, var3)), Z(*res))


class TestEngineProductable(unittest.TestCase):
    """Test behaviour of the engine with Productables.
    """
    def test_engine_productable_productable(self):
        """Tests the behaviour of the engine on non nested Productables.
        """
        var1 = P(1, 2, 3)
        var2 = P(4, 5, 6)
        var3 = P(7, 8, 9)
        var4 = P(10, 11, 12)
        self.assertEqual(list(engine(var1, var2, var3, var4)),
                         list(grouper(flatten(var1 + var2 + var3 + var4), 4)))

    def test_engine_nested_productable(self):
        """Tests the behaviour of the engine on nested Productables.
        """
        var1 = P(P(1, 2, 3), P(4, 5, 6))
        var2 = P(P(7, 8, 9), P(10, 11, 12))
        self.assertEqual(set(list(engine(var1, var2))),
                         set(list(product([1, 2, 3, 4, 5, 6],
                                          [7, 8, 9, 10, 11, 12]))))

    def test_engine_nested_productable_3(self):
        """Tests the behaviour of the engine on 3 nested Productables.
        """
        var1 = P(P(1, 2, 3), P(4, 5, 6))
        var2 = P(P(7, 8, 9), P(10, 11, 12))
        var3 = P(P(13, 14, 15), P(16, 17, 18))
        res = product([1, 2, 3, 4, 5, 6],
                      [7, 8, 9, 10, 11, 12],
                      [13, 14, 15, 16, 17, 18])
        self.assertEqual(set(list(engine(var1, var2, var3))), set(list(res)))


class TestEngineMixing(unittest.TestCase):
    """Test the behaviour of the engine with mixtures of Zipables & Productables.
    """
    def test_engine_mixing(self):
        """Tests the behaviour of the engine on a mixture of Zipables and
        Productables.
        """
        var1 = Z(1, 2)
        var2 = Z(3, 4)
        var3 = P(5, 6)
        res = [(1, 3, 5), (1, 3, 6), (2, 4, 5), (2, 4, 6)]
        self.assertEqual(list(engine(var1, var2, var3)), res)

    def test_engine_mixing_nested(self):
        """Tests the behaviour of the engine on a mixture of nested Zipables
        and Productables.
        """
        var1 = P(Z(1, 2), P(3, 4))
        var2 = P(Z(5, 6), P(7, 8))
        var3 = P(P(9, 10), P(11, 12))
        res = [(1, 5, 9),
               (1, 5, 10),
               (2, 6, 9),
               (2, 6, 10),
               (1, 5, 11),
               (1, 5, 12),
               (2, 6, 11),
               (2, 6, 12),
               (1, 7, 9),
               (1, 7, 10),
               (1, 8, 9),
               (1, 8, 10),
               (2, 7, 9),
               (2, 7, 10),
               (2, 8, 9),
               (2, 8, 10),
               (1, 7, 11),
               (1, 7, 12),
               (1, 8, 11),
               (1, 8, 12),
               (2, 7, 11),
               (2, 7, 12),
               (2, 8, 11),
               (2, 8, 12),
               (3, 5, 9),
               (3, 5, 10),
               (3, 6, 9),
               (3, 6, 10),
               (4, 5, 9),
               (4, 5, 10),
               (4, 6, 9),
               (4, 6, 10),
               (3, 5, 11),
               (3, 5, 12),
               (3, 6, 11),
               (3, 6, 12),
               (4, 5, 11),
               (4, 5, 12),
               (4, 6, 11),
               (4, 6, 12),
               (3, 7, 9),
               (3, 7, 10),
               (3, 8, 9),
               (3, 8, 10),
               (4, 7, 9),
               (4, 7, 10),
               (4, 8, 9),
               (4, 8, 10),
               (3, 7, 11),
               (3, 7, 12),
               (3, 8, 11),
               (3, 8, 12),
               (4, 7, 11),
               (4, 7, 12),
               (4, 8, 11),
               (4, 8, 12)]
        self.assertEqual(list(engine(var1, var2, var3)), res)


class TestEngineUtils(unittest.TestCase):
    """Test the behaviour of the helper functions.
    """
    def test_flatten(self):
        """Tests the behaviour of helper flatten."""
        inp = ((1, 2), (3, (4, 5)))
        self.assertEqual(list(flatten(inp)), [1, 2, 3, 4, 5])

    def test_grouper(self):
        """Tests the behaviour of helper grouper."""
        inp = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(list(grouper(inp, 2)),
                         [(1, 2), (3, 4), (5, 6), (7, 8)])
