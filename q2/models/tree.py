from decimal import Decimal
from typing import List

from models.specdata import Metabolite, Adduct


class Node:

    def __init__(self, entry: Metabolite | Adduct, left: 'Node', right: 'Node'):
        self.entry = entry
        self.left = left
        self.right = right

    def get_data(self) -> Decimal:
        return self.entry.data


class Tree:

    def __init__(self, entries: List[Metabolite] | List[Adduct]):
        self.root = None
        self.num_nodes = 0

        # Sort entries to create balanced tree
        entries = sorted(entries, key=lambda x: x.data)

        def add_middle(first_index, last_index):
            middle_index = (last_index + first_index) // 2
            entry_middle = entries[middle_index]

            self.add(entry_middle)
            
            # Recursively build left branch
            if first_index != middle_index:
                add_middle(first_index, middle_index - 1)
            # Recursively build right branch
            if middle_index != last_index:
                add_middle(middle_index + 1, last_index)

        add_middle(0, len(entries) - 1)

    def add(self, entry: Metabolite | Adduct):
        if self.root is None:
            self.root = Node(
                entry=entry,
                left=None,
                right=None,
            )
        else:
            self._add(entry, self.root)

        self.num_nodes += 1
    
    def _add(self, entry: Metabolite | Adduct, node: Node):
        if entry.data < node.get_data():
            if node.left is not None:
                self._add(entry, node.left)
            else:
                node.left = Node(
                    entry=entry,
                    left=None,
                    right=None,
                )
        else:
            if node.right is not None:
                self._add(entry, node.right)
            else:
                node.right = Node(
                    entry=entry,
                    left=None,
                    right=None,
                )

    def find(self, target: Decimal) -> Metabolite | Adduct:
        if self.root is not None:
            closest = type(self.root.entry)(idx=0, data=Decimal('Inf'))
            return self._find(target, self.root, closest)

    def _find(self, target: Decimal, node: Node, closest: Metabolite | Adduct) -> Metabolite | Adduct:
        if node.get_data() == target:
            return node.entry

        if abs(target - node.get_data()) <= abs(target - closest.data):
            closest = node.entry

        if node.left is None and node.right is None:
            return closest
        elif target < node.get_data():
            if node.left is None:
                return closest
            return self._find(target, node.left, closest)
        elif target > node.get_data():
            if node.right is None:
                return closest
            return self._find(target, node.right, closest)