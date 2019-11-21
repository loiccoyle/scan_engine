import unittest
from itertools import product
from scan_engine import Productable as P
from scan_engine import Zipable as Z


class testZipable(unittest.TestCase):
    def test_Zipable_Zipable(self):
        '''Behaviour when Zipable conbines another Zipable.
        '''
        var1 = Z(1, 2, 3)
        var2 = Z(4, 5, 6)
        self.assertEqual(var1 + var2, Z(*zip(var1, var2)))

    def test_Zipable_standard(self):
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


    def test_Zipable_iterator(self):
        '''Behaviour when Zipable combines with tuple or list.
        '''
        var1 = Z(1, 2, 3)
        var2 = (4, 5)
        self.assertEqual(var1 + var2, Z((1, var2), (2, var2), (3, var2)))

        var1 = Z(1, 2, 3)
        var2 = [4, 5]
        self.assertEqual(var1 + var2, Z((1, var2), (2, var2), (3, var2)))


class testProductable(unittest.TestCase):
    def test_Productable_Productable(self):
        '''Behaviour when Productable conbines another Productable.
        '''
        var1 = P(1, 2, 3)
        var2 = P(4, 5, 6)
        self.assertEqual(var1 + var2, P(*product(var1, var2)))

    def test_Productable_standard(self):
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


    def test_Productable_iterator(self):
        '''Behaviour when Productable combines with tuple or list.
        '''
        var1 = P(1, 2, 3)
        var2 = (4, 5)
        self.assertEqual(var1 + var2, P((1, var2), (2, var2), (3, var2)))

        var1 = P(1, 2, 3)
        var2 = [4, 5]
        self.assertEqual(var1 + var2, P((1, var2), (2, var2), (3, var2)))

class testMixing(unittest.TestCase):
    def test_mixing(self):
        '''Behaviour when combining Productable and Zipable.
        '''
        var1 = Z(1, 2, 3)
        var2 = P(4, 5, 6)
        self.assertEqual(var1 + var2, P(*var1) + var2)


