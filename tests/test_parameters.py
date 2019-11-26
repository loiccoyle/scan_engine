'''parameters.py unit tests.
'''
import unittest
from itertools import product
from scan_engine import Productable as P
from scan_engine import Zipable as Z


class TestZipable(unittest.TestCase):
    '''Test behaviour of Zipable.
    '''
    def test_zipable_zipable(self):
        '''Behaviour when Zipable conbines another Zipable.
        '''
        var1 = Z(1, 2, 3)
        var2 = Z(4, 5, 6)
        self.assertEqual(var1 + var2, Z(*zip(var1, var2)))

    def test_zipable_standard(self):
        '''Behaviour when Zipable combines with standard types.
        '''
        var1 = Z(1, 2, 3)
        var2 = 1
        self.assertEqual(var1 + var2, Z((1, var2), (2, var2), (3, var2)))

        var1 = Z(1, 2, 3)
        var2 = 1.1
        self.assertEqual(var1 + var2, Z((1, var2), (2, var2), (3, var2)))

        var1 = Z(1, 2, 3)
        var2 = 'aa'
        self.assertEqual(var1 + var2, Z((1, var2), (2, var2), (3, var2)))

    def test_zipable_iterator(self):
        '''Behaviour when Zipable combines with tuple or list.
        '''
        var1 = Z(1, 2, 3)
        var2 = (4, 5)
        self.assertEqual(var1 + var2, Z((1, var2), (2, var2), (3, var2)))

        var1 = Z(1, 2, 3)
        var2 = [4, 5]
        self.assertEqual(var1 + var2, P((1, 4), (1, 5),
                                        (2, 4), (2, 5),
                                        (3, 4), (3, 5)))


class TestProductable(unittest.TestCase):
    '''Test behaviour of Productable.
    '''
    def test_productable_productable(self):
        '''Behaviour when Productable conbines another Productable.
        '''
        var1 = P(1, 2, 3)
        var2 = P(4, 5, 6)
        self.assertEqual(var1 + var2, P(*product(var1, var2)))

    def test_productable_standard(self):
        '''Behaviour when Productable combines with standard types.
        '''
        var1 = P(1, 2, 3)
        var2 = 1
        self.assertEqual(var1 + var2, P((1, var2), (2, var2), (3, var2)))

        var1 = P(1, 2, 3)
        var2 = 1.1
        self.assertEqual(var1 + var2, P((1, var2), (2, var2), (3, var2)))

        var1 = P(1, 2, 3)
        var2 = 'aa'
        self.assertEqual(var1 + var2, P((1, var2), (2, var2), (3, var2)))

    def test_productable_iterator(self):
        '''Behaviour when Productable combines with tuple or list.
        '''
        var1 = P(1, 2, 3)
        var2 = (4, 5)
        self.assertEqual(var1 + var2, P((1, var2), (2, var2), (3, var2)))

        var1 = P(1, 2, 3)
        var2 = [4, 5]
        self.assertEqual(var1 + var2, P((1, 4), (1, 5),
                                        (2, 4), (2, 5),
                                        (3, 4), (3, 5)))


class TestMixing(unittest.TestCase):
    '''Test behaviour of Zipable & Productable mixing.
    '''
    def test_mixing(self):
        '''Behaviour when combining Productable and Zipable.
        '''
        var1 = Z(1, 2, 3)
        var2 = P(4, 5, 6)
        self.assertEqual(var1 + var2, P(*var1) + var2)
