import unittest
from functions import *


class MyTestCase(unittest.TestCase):
    def test_letter_grade(self):
        self.assertEqual(letter_grade(93), 'A')
        self.assertEqual(letter_grade(86), 'B')
        self.assertEqual(letter_grade(73), 'C')
        self.assertEqual(letter_grade(69), 'D')
        self.assertEqual(letter_grade(35), 'F')
        self.assertEqual(letter_grade(-8), False)
        self.assertEqual(letter_grade(892), False)
        self.assertEqual(letter_grade('Jo'), False)

    def test_conversion(self):
        self.assertEqual(conversion('A'), 4)
        self.assertEqual(conversion('B'), 3)
        self.assertEqual(conversion('C'), 2)
        self.assertEqual(conversion('D'), 1)
        self.assertEqual(conversion('F'), 0)

    def test_average(self):
        self.assertAlmostEqual(average(4), 4)
        self.assertAlmostEqual(average(4, 3), 3.5)
        self.assertAlmostEqual(average(4, 3, 2), 3)
        self.assertAlmostEqual(average(4, 4, 3, 3), 3.5)
        self.assertAlmostEqual(average(3, 2, 4, 2, 1, 4, 3, 2, 0, 1), 2.2)


if __name__ == '__main__':
    unittest.main()
