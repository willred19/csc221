import unittest

from year import is_leap_year

class YearTest(unittest.TestCase):
    def test_year(self):
        self.assertTrue(is_leap_year(1896))

    def test_is_leap_year(self):
        self.assertFalse(is_leap_year(2015))

    def test_is_leap_year(self):
        self.assertFalse(is_leap_year(2003))




from dna import to_rna
class DnaTest(unittest.TestCase):
    def test_thymine_to_adedine_dna(self):
        self.assertEqual('T', to_rna('A'))
        self.assertEqual('t', to_rna('a'))

    def test_guanine_to_cytosine_dna(self):
        self.assertEqual('G', to_rna('C'))
        self.assertEqual('g', to_rna('c'))

    def test_adenine_to_uracil_dna(self):
        self.assertEqual('A', to_rna('U'))
        self.assertEqual('a', to_rna('U'))

    def test_combinations_dna(self):
        self.assertEqual('ggcc', to_rna('ccgg'))
        self.assertEqual('Ta gC', to_rna('Au cG'))


from count import rna_count

class CountTest(unittest.TestCase):
    def test_rna_count(self):
        self.assertEqual(
            {'A': 2, 'c': 3, 'U': 1, 'T': 4},
            rna_count('AAcccUTTTT'))