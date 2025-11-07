from typing import Any


class Queue:
    # Creates an empty queue.
    def __init__(self) -> None:
        self._q_list: list[Any] = list()

    # Returns True if the queue is empty.
    def is_empty(self) -> bool:
        return len(self._q_list) == 0

    # Return the number of items in the queue.
    def __len__(self) -> int:
        return len(self._q_list)

    # Adds the given item to the queue.
    def enqueue(self, item: Any):
        self._q_list.append(item)

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        return self._q_list.pop(0)
