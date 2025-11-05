from typing import Any, TypeVar

T = TypeVar('T')

# Implementation of the Set ADT container using Python list.


class Set[T]:
    # Create an empty se instance.
    def __init__(self) -> None:
        self._elements: list[T] = list()

    # Returns the  number of items in the set.
    def __len__(self) -> int:
        return len(self._elements)

    # Determines if an element is in the set.
    def __contains__(self, element: Any):
        return element in self._elements

    # Adds a new unique element to the set.
    def add(self, element: Any):
        if element not in self:
            self._elements.append(element)

    # Removes an element from the set.
    def remove(self, element: Any):
        assert element in self, "The element must be in the set."
        self._elements.remove(element)

    # Returns an iterator for the set.
    def __iter__(self):
        return iter(self._elements)

    # Determines if two sets are equal
    def __eq__(self, set_b: "Set[T]") -> bool:
        if len(self) != len(set_b):
            return False
        return self.is_subset_of(set_b)

    # Determines if this set is a subset of setB
    def is_subset_of(self, set_b: "Set[T]") -> bool:
        for element in self:
            if element not in set_b:
                return False
        return True

    # Creates a new set from the union of this set and setB
    def union(self, set_b: "Set[T]") -> "Set[T]":
        new_set = Set[T]()
        new_set._elements.extend(self._elements)

        for element in set_b:
            if element not in self:
                new_set._elements.append(element)
        return new_set

    # Creates a new set form the intersection: self set and setB
    def intersect(self, set_b: "Set[T]"):
        pass
