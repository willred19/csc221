import unittest

from year import is_leap_year

class YearTest(unittest.TestCase):
    def test_year(self):
        self.assertTrue(is_leap_year(1896))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(2015))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(2003))







if __name__ =='__main__':
    unittest.main()