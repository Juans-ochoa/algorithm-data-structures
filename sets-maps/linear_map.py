from typing import Any, Self


intOrString = int | str
typeValue = int | str | float | bool | object

# Implementation of Map ADT using a single list.


class Map:
    # Creates an empty map instance.
    def __init__(self) -> None:
        self._entry_list: list["_MapEntry"] = list()

    # Returns the number of entries in the map.
    def __len__(self) -> int:
        return len(self._entry_list)

    # Determines if the man contains the given key.
    def __contains__(self, key: intOrString) -> bool:
        ndx = self._find_position(key)
        return ndx is not None

    # Adds a new entry to the map if the key does exist. Otherwise, the new value replaces the current value associated with the key.

    def add(self, key: intOrString, value: typeValue) -> bool:
        ndx = self._find_position(key)

        if ndx is not None:
            self._entry_list[ndx].value = value
            return False
        else:  # Otherwise add a new entry
            entry = _MapEntry(key, value)
            self._entry_list.append(entry)
            return True

    # Returns the value associated with the key.
    def value_of(self, key: intOrString) -> typeValue:
        ndx = self._find_position(key)
        assert ndx is not None, "Invalid map key."
        return self._entry_list[ndx].value

    # Removes the entry associated with the key.
    def remove(self, key: Any):
        ndx = self._find_position(key)
        assert ndx is not None, "Invalid map Key"
        self._entry_list.pop(ndx)

    # Helper method used tof ind the index position of a category. If the key is not found, None is returned.
    def _find_position(self, key: Any) -> int | None:
        # Iterate through each entry in the list.
        for i in range(len(self)):
            # Is the key stored in the ith entry?
            if self._entry_list[i] == key:
                return i
        return None

    # Returns an iterator for traversing the keys in the map.
    def __iter__(self):
        return _MapIterator(self._entry_list)


# Storage class for holding the key/value pairs


class _MapEntry:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value


# Iterator
class _MapIterator:
    def __init__(self, map: list["_MapEntry"]) -> None:
        self._map_ref = map
        self._cur_index = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> typeValue:
        if self._cur_index < len(self._map_ref):
            entry = self._map_ref[self._cur_index]
            self._cur_index += 1
            return entry.value  # type: ignore

        raise StopIteration
