from typing import NamedTuple
import unittest

from decimal import Decimal

from models.specdata import Adduct
from models.tree import Tree


class TestTree(unittest.TestCase):

    def test_init_tree(self):
        entries = [
            Adduct(idx=1, data=Decimal('1')),  # entry 0
            Adduct(idx=2, data=Decimal('9')),  # entry 1
            Adduct(idx=3, data=Decimal('4')),  # entry 2
            Adduct(idx=4, data=Decimal('2')),  # entry 3
            Adduct(idx=5, data=Decimal('8')),  # entry 4
            Adduct(idx=6, data=Decimal('3')),  # entry 5
            Adduct(idx=7, data=Decimal('5')),  # entry 6
            Adduct(idx=8, data=Decimal('6')),  # entry 7
            Adduct(idx=9, data=Decimal('10')),  # entry 8
            Adduct(idx=10, data=Decimal('7')),  # entry 9
        ]

        tree = Tree(entries)

        self.assertEqual(tree.num_nodes, len(entries))

        self.assertEqual(tree.root.entry, entries[6])  # Data: 5
        # Left branch
        self.assertEqual(tree.root.left.entry, entries[3])  # Data: 2
        self.assertEqual(tree.root.left.left.entry, entries[0])  # Data: 1
        self.assertEqual(tree.root.left.left.left, None)
        self.assertEqual(tree.root.left.left.right, None)
        self.assertEqual(tree.root.left.right.entry, entries[5])  # Data: 3
        self.assertEqual(tree.root.left.right.left, None)
        self.assertEqual(tree.root.left.right.right.entry, entries[2])  # Data: 4
        self.assertEqual(tree.root.left.right.right.left, None)
        self.assertEqual(tree.root.left.right.right.right, None)
        # Right branch
        self.assertEqual(tree.root.right.entry, entries[4])  # Data: 8
        self.assertEqual(tree.root.right.left.entry, entries[7])  # Data: 6
        self.assertEqual(tree.root.right.left.left, None)
        self.assertEqual(tree.root.right.left.right.entry, entries[9])  # Data: 7
        self.assertEqual(tree.root.right.left.right.left, None)
        self.assertEqual(tree.root.right.left.right.right, None)
        self.assertEqual(tree.root.right.right.entry, entries[1])  # Data: 9
        self.assertEqual(tree.root.right.right.left, None)
        self.assertEqual(tree.root.right.right.right.entry, entries[8])  # Data: 10
        self.assertEqual(tree.root.right.right.right.left, None)
        self.assertEqual(tree.root.right.right.right.right, None)

    def test_find_within_tree(self):
        entries = [
            Adduct(idx=1, data=Decimal('1')),  # entry 0
            Adduct(idx=2, data=Decimal('9')),  # entry 1
            Adduct(idx=3, data=Decimal('4')),  # entry 2
            Adduct(idx=4, data=Decimal('2')),  # entry 3
            Adduct(idx=5, data=Decimal('8')),  # entry 4
            Adduct(idx=6, data=Decimal('3')),  # entry 5
            Adduct(idx=7, data=Decimal('5')),  # entry 6
            Adduct(idx=8, data=Decimal('6')),  # entry 7
            Adduct(idx=9, data=Decimal('10')),  # entry 8
            Adduct(idx=10, data=Decimal('7')),  # entry 9
        ]

        tree = Tree(entries)

        class Case(NamedTuple):
            target: Decimal
            expected: Adduct
        
        cases = [
            Case(
                target=Decimal('1'),
                expected=entries[0],
            ),
            Case(
                target=Decimal('1.1'),
                expected=entries[0],
            ),
            Case(
                target=Decimal('1.499999'),
                expected=entries[0],
            ),
            Case(
                target=Decimal('1.500000'),
                expected=entries[0],
            ),
            Case(
                target=Decimal('1.500001'),
                expected=entries[3],
            ),
            Case(
                target=Decimal('0.1'),
                expected=entries[0],
            ),
            Case(
                target=Decimal('-100'),
                expected=entries[0],
            ),
            Case(
                target=Decimal('3.1'),
                expected=entries[5],
            ),
            Case(
                target=Decimal('2.9'),
                expected=entries[5],
            ),
            Case(
                target=Decimal('5'),
                expected=entries[6],
            ),
            Case(
                target=Decimal('5.4'),
                expected=entries[6],
            ),
            Case(
                target=Decimal('10000'),
                expected=entries[8],
            ),
            Case(
                target=Decimal('6'),
                expected=entries[7],
            ),
            Case(
                target=Decimal('6.4'),
                expected=entries[7],
            ),
            Case(
                target=Decimal('5.6'),
                expected=entries[7],
            ),
            Case(
                target=Decimal('8.9'),
                expected=entries[1],
            ),
            Case(
                target=Decimal('9'),
                expected=entries[1],
            ),
            Case(
                target=Decimal('9.3214'),
                expected=entries[1],
            ),
        ]

        for c in cases:
            got = tree.find(c.target)
            self.assertEqual(got, c.expected)

    def test_case_from_toy_set_2(self):
        entries = [
            Adduct(idx=1, data=Decimal('0.500000')),
            Adduct(idx=2, data=Decimal('-0.500000')),
        ]

        tree = Tree(entries)
        target = Decimal('-1.000001')

        got = tree.find(target)
        self.assertEqual(got, entries[1])

    def test_case_2_from_toy_set_2(self):
        entries = [
            Adduct(idx=1, data=Decimal('0.500000')),
            Adduct(idx=2, data=Decimal('-0.500000')),
        ]

        tree = Tree(entries)
        target = Decimal('0.000000')

        got = tree.find(target)
        self.assertEqual(got, entries[0])