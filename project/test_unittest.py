import unittest

from year import is_leap_year

class YearTest(unittest.TestCase):
    def test_year(self):
        self.assertTrue(is_leap_year(1896))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(2015))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(2003))



from dna import to_rna
def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual('C', to_rna('G'))

def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual('G', to_rna('C'))

def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual('A', to_rna('T'))

def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual('U', to_rna('A'))




if __name__ =='__main__':
    unittest.main()