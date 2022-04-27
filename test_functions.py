import unittest
from functions import *


class MyTestCase(unittest.TestCase):
    def test_valid_score(self):
        """test to check outputs of valid_score"""
        self.assertEqual(valid_score(5), 5)
        self.assertEqual(valid_score(.5),.5)
        self.assertEqual(valid_score(-23), False)
        self.assertEqual(valid_score('one'), False)
        self.assertEqual(valid_score(123), False)

    def test_average(self):
        """test average function"""
        self.assertEqual(average([10, 20, 30]), 20)
        self.assertAlmostEqual(average([20.5, 30.5, 40.5]), 30.5)

    def test_letter_grade(self):
        """test letter grade function"""
        self.assertEqual(letter_grade(94), 'A')
        self.assertEqual(letter_grade(83), 'B')
        self.assertEqual(letter_grade(75), 'C')
        self.assertEqual(letter_grade(69), 'D')
        self.assertEqual(letter_grade(23), 'F')


if __name__ == '__main__':
    unittest.main()
