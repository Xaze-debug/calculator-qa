import unittest
from division_case import divide

class TestDivisionContract(unittest.TestCase):

    def test_positive_numbers(self):
        # divide(8, 2) -> 4
        self.assertAlmostEqual(divide(8, 2), 4)

    def test_float_result(self):
        # divide(7, 2) -> 3.5
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_negative_numbers(self):
        # divide(-6, 2) -> -3
        self.assertAlmostEqual(divide(-6, 2), -3)

    def test_zero_numerator(self):
        # divide(0, 5) -> 0
        self.assertAlmostEqual(divide(0, 5), 0)

    def test_division_by_zero(self):
        # divide(5, 0) -> ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_zero_by_zero(self):
        # divide(0, 0) -> ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)

if __name__ == '__main__':
    unittest.main()
