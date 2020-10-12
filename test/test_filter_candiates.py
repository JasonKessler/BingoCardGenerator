import unittest

from bingocardgenerator.square_getter import filter_candidates


class TestFilterCanidates(unittest.TestCase):
    def test_filter_unique_candidates_returns_identity(self):
        self.assertEqual(filter_candidates(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_filter_redundant_candidates(self):
        self.assertEqual(filter_candidates(['a', 'a b', 'b', 'c', 'b c']), ['a b', 'b c'])

    def test_filter_later_candidates(self):
        self.assertEqual(filter_candidates(['a b c', 'a b', 'b c']), ['a b c'])


if __name__ == '__main__':
    unittest.main()
