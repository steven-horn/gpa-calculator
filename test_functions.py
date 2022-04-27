import unittest
from functions import *


class MyTestCase(unittest.TestCase):
    def test_valid_score(self):
        """test to check outputs of valid_score"""
        self.assertEqual(valid_score(5), 5)
        self.assertEqual(valid_score(-23), False)
        self.assertEqual(valid_score('one'), False)


if __name__ == '__main__':
    unittest.main()
