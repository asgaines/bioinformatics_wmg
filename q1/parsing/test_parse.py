import io
import unittest

from parsing import parse


class TestParseSequences(unittest.TestCase):

    def test_empty_file_yields_only_final_data(self):
        expected = [
            parse.LineData(N=0, sequence=[], new_start=True),
        ]

        with io.StringIO() as f:
            f.seek(0)

            got = list(parse.sequences(f))

        self.assertEqual(expected, got)


    def test_single_sequence_correct_yield(self):
        expected = [
            parse.LineData(N=5, sequence=[], new_start=True),
            parse.LineData(N=-1, sequence=[1, 2, 3, 5], new_start=False),
            parse.LineData(N=0, sequence=[], new_start=True),
        ]

        with io.StringIO() as f:
            f.write('>5\n')
            f.write('1 2 3 5\n')
            f.seek(0)

            got = list(parse.sequences(f))

        self.assertEqual(expected, got)


    def test_two_sequences_correct_yield(self):
        expected = [
            parse.LineData(N=5, sequence=[], new_start=True),
            parse.LineData(N=-1, sequence=[1, 2, 3, 5], new_start=False),
            parse.LineData(N=15, sequence=[], new_start=True),
            parse.LineData(N=-1, sequence=[1, 2, 3, 4, 5, 7, 8, 9, 10], new_start=False),
            parse.LineData(N=-1, sequence=[11, 12, 13, 14, 15], new_start=False),
            parse.LineData(N=0, sequence=[], new_start=True),
        ]

        with io.StringIO() as f:
            f.write('>5\n')
            f.write('1 2 3 5\n')
            f.write('>15\n')
            f.write('1 2 3 4 5 7 8 9 10\n')
            f.write('11 12 13 14 15\n')
            f.seek(0)

            got = list(parse.sequences(f))

        self.assertEqual(expected, got)