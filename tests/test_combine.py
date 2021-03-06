"""combine.py unit tests.
"""
import unittest
from itertools import product
from scan_engine import Productable as P
from scan_engine import Zipable as Z
from scan_engine import combine

from scan_engine.combine import flatten
from scan_engine.combine import grouper
from scan_engine.combine import expand
from scan_engine.combine import check_for_params


class TestEngineDefaults(unittest.TestCase):
    """Test behaviour of the combine function with lists and tuples.
    """
    def test_engine_lists(self):
        """Tests the behviour of the combine function with standard lists. Should be cast
        to Productables.
        """
        var1 = [1, 2]
        var2 = [3, 4]
        self.assertEqual(list(combine(var1, var2)),
                         [(1, 3), (1, 4), (2, 3), (2, 4)])

    def test_engine_tuples(self):
        """Tests the behviour of the combine function with standard tuples. Should be left as is.
        """
        var1 = [1, 2]
        var2 = (3, 4)
        self.assertEqual(list(combine(var1, var2)), [(1, (3, 4)), (2, (3, 4))])

    def test_engine_tuples_mixing(self):
        """Tests the behviour of the combine function with standard tuples
        alongside Zipables and Productables.
        """
        var1 = P(Z(1, 2), P(3, 4))
        var2 = P(Z(5, 6), P(7, 8))
        var3 = ('weirdo!', 5)
        res = [(1, 5, ('weirdo!', 5)),
               (2, 6, ('weirdo!', 5)),
               (1, 7, ('weirdo!', 5)),
               (1, 8, ('weirdo!', 5)),
               (2, 7, ('weirdo!', 5)),
               (2, 8, ('weirdo!', 5)),
               (3, 5, ('weirdo!', 5)),
               (3, 6, ('weirdo!', 5)),
               (4, 5, ('weirdo!', 5)),
               (4, 6, ('weirdo!', 5)),
               (3, 7, ('weirdo!', 5)),
               (3, 8, ('weirdo!', 5)),
               (4, 7, ('weirdo!', 5)),
               (4, 8, ('weirdo!', 5))]
        self.assertEqual(list(combine(var1, var2, var3)), res)


class TestEngineZipable(unittest.TestCase):
    """Test behaviour of the combine function with Zipables.
    """
    def test_engine_zipable_zipable(self):
        """Tests the behaviour of the combine function on non nested Zipables.
        """
        var1 = Z(1, 2, 3)
        var2 = Z(4, 5, 6)
        var3 = Z(7, 8, 9)
        var4 = Z(10, 11, 12)
        self.assertEqual(list(combine(var1, var2, var3, var4)),
                         list(grouper(flatten(var1 + var2 + var3 + var4), 4)))

    def test_engine_nested_zipable(self):
        """Tests the behaviour of the combine function on nested Zipables.
        """
        var1 = Z(Z(1, 2, 3), Z(4, 5, 6))
        var2 = Z(Z(7, 8, 9), Z(10, 11, 12))
        self.assertEqual(list(combine(var1, var2)),
                         Z(*zip([1, 2, 3, 4, 5, 6],
                                [7, 8, 9, 10, 11, 12])))

    def test_engine_nested_zipable_3(self):
        """Tests the behaviour of the combine function on 3 nested Zipables.
        """
        var1 = Z(Z(1, 2, 3), Z(4, 5, 6))
        var2 = Z(Z(7, 8, 9), Z(10, 11, 12))
        var3 = Z(Z(13, 14, 15), Z(16, 17, 18))
        res = zip([1, 2, 3, 4, 5, 6],
                  [7, 8, 9, 10, 11, 12],
                  [13, 14, 15, 16, 17, 18])
        self.assertEqual(list(combine(var1, var2, var3)), Z(*res))


class TestEngineProductable(unittest.TestCase):
    """Test behaviour of the combine function with Productables.
    """
    def test_engine_productable_productable(self):
        """Tests the behaviour of the combine function on non nested Productables.
        """
        var1 = P(1, 2, 3)
        var2 = P(4, 5, 6)
        var3 = P(7, 8, 9)
        var4 = P(10, 11, 12)
        self.assertEqual(list(combine(var1, var2, var3, var4)),
                         list(grouper(flatten(var1 + var2 + var3 + var4), 4)))

    def test_engine_nested_productable(self):
        """Tests the behaviour of the combine function on nested Productables.
        """
        var1 = P(P(1, 2, 3), P(4, 5, 6))
        var2 = P(P(7, 8, 9), P(10, 11, 12))
        self.assertEqual(set(list(combine(var1, var2))),
                         set(list(product([1, 2, 3, 4, 5, 6],
                                          [7, 8, 9, 10, 11, 12]))))

    def test_engine_nested_productable_3(self):
        """Tests the behaviour of the combine function on 3 nested Productables.
        """
        var1 = P(P(1, 2, 3), P(4, 5, 6))
        var2 = P(P(7, 8, 9), P(10, 11, 12))
        var3 = P(P(13, 14, 15), P(16, 17, 18))
        res = product([1, 2, 3, 4, 5, 6],
                      [7, 8, 9, 10, 11, 12],
                      [13, 14, 15, 16, 17, 18])
        self.assertEqual(set(list(combine(var1, var2, var3))), set(list(res)))


class TestEngineMixing(unittest.TestCase):
    """Test the behaviour of the combine function with mixtures of Zipables & Productables.
    """
    def test_engine_mixing(self):
        """Tests the behaviour of the combine function on a mixture of Zipables and
        Productables.
        """
        var1 = Z(1, 2)
        var2 = Z(3, 4)
        var3 = P(5, 6)
        res = [(1, 3, 5), (1, 3, 6), (2, 4, 5), (2, 4, 6)]
        self.assertEqual(list(combine(var1, var2, var3)), res)

    def test_engine_mixing_nested(self):
        """Tests the behaviour of the combine function on a mixture of nested Zipables
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
        self.assertEqual(list(combine(var1, var2, var3)), res)

    def test_egine_mixing_nested_2(self):
        """Tests the behaviour of the combine function on a mixture of nested Zipables
        and Productables.
        """
        var1 = Z(2, 3)
        var2 = Z(2, 3)
        var3 = Z(P(10, 11), P(12, 13))
        var4 = P(20, 21)
        var5 = P(22, 23)
        expected = [(2, 2, 10, 20, 22),
                    (2, 2, 11, 20, 22),
                    (2, 2, 10, 20, 23),
                    (2, 2, 11, 20, 23),
                    (2, 2, 10, 21, 22),
                    (2, 2, 11, 21, 22),
                    (2, 2, 10, 21, 23),
                    (2, 2, 11, 21, 23),
                    (3, 3, 12, 20, 22),
                    (3, 3, 13, 20, 22),
                    (3, 3, 12, 20, 23),
                    (3, 3, 13, 20, 23),
                    (3, 3, 12, 21, 22),
                    (3, 3, 13, 21, 22),
                    (3, 3, 12, 21, 23),
                    (3, 3, 13, 21, 23)]
        self.assertEqual(list(combine(var1, var2, var3, var4, var5)),
                         expected)

    def test_egine_mixing_nested_3(self):
        """Tests the behaviour of the combine function on a mixture of nested Zipables
        and Productables.
        """
        var1 = Z(1, 2, 3)
        var2 = Z(1, 2, 3)
        var3 = P(10, 11, 12)
        var4 = P(13, 14, 15)
        expected = [(1, 1, 10, 13),
                    (1, 1, 10, 14),
                    (1, 1, 10, 15),
                    (1, 1, 11, 13),
                    (1, 1, 11, 14),
                    (1, 1, 11, 15),
                    (1, 1, 12, 13),
                    (1, 1, 12, 14),
                    (1, 1, 12, 15),
                    (2, 2, 10, 13),
                    (2, 2, 10, 14),
                    (2, 2, 10, 15),
                    (2, 2, 11, 13),
                    (2, 2, 11, 14),
                    (2, 2, 11, 15),
                    (2, 2, 12, 13),
                    (2, 2, 12, 14),
                    (2, 2, 12, 15),
                    (3, 3, 10, 13),
                    (3, 3, 10, 14),
                    (3, 3, 10, 15),
                    (3, 3, 11, 13),
                    (3, 3, 11, 14),
                    (3, 3, 11, 15),
                    (3, 3, 12, 13),
                    (3, 3, 12, 14),
                    (3, 3, 12, 15)]
        self.assertEqual(list(combine(var1, var2, var3, var4)),
                         expected)


class TestEngineUtils(unittest.TestCase):
    """Test the behaviour of the helper functions.
    """

    def test_expand(self):
        """Tests the behaviour of helper expand."""
        var1 = P(Z(1, 2, 3), Z(4, 5, 6))
        var2 = P(Z(7, 8, 9), Z(10, 11, 12))
        expanded = list(expand((var1 + var2)[0]))
        self.assertEqual(expanded, [Z((1, 7), (2, 8), (3, 9))])

    def test_flatten(self):
        """Tests the behaviour of helper flatten."""
        var1 = P(Z(1, 2, 3), Z(4, 5, 6))
        var2 = P(Z(7, 8, 9), Z(10, 11, 12))
        expanded = list(expand((var1 + var2)[0]))
        self.assertEqual(list(flatten(expanded)), [1, 7, 2, 8, 3, 9])

    def test_grouper(self):
        """Tests the behaviour of helper grouper."""
        inp = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(list(grouper(inp, 2)),
                         [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_check_for_params(self):
        """Tests the nested param check helper."""
        inp = ((((Z(1), 0), P(1)), 0), 0)
        self.assertEqual(sum(check_for_params(inp)), 2)
