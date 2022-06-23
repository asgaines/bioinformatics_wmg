import unittest

from process import search


class TestFindMissing(unittest.TestCase):

    def test_given_sample_data(self):
        expected = [
            search.Result(N=10, missing=7),
            search.Result(N=1000, missing=435),
        ]
        got = search.find_missing('./flatfiles/question_one.txt')

        self.assertEqual(got, expected)

    def test_empty_data(self):
        expected = []
        got = search.find_missing('./flatfiles/empty.txt')

        self.assertEqual(got, expected)

    def test_single_sequence_1_line(self):
        expected = [
            search.Result(N=10, missing=7),
        ]
        got = search.find_missing('./flatfiles/single_sequence_1_line.txt')

        self.assertEqual(got, expected)

    def test_2_large_seqs_1_small(self):
        expected = [
            search.Result(N=512459, missing=33941),
            search.Result(N=50, missing=42),
            search.Result(N=1000000, missing=712955),
        ]
        got = search.find_missing('./flatfiles/2_large_sequences_1_small.txt')

        self.assertEqual(got, expected)

    def test_largest_seq(self):
        expected = [
            search.Result(N=10000000, missing=6897133),
        ]
        got = search.find_missing('./flatfiles/largest.txt')

        self.assertEqual(got, expected)