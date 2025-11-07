from typing import Any
from arrays.array import Array


class Queue:
    # Create an empty queue.
    def __init__(self, max_size: int) -> None:
        self._count = 0
        self._front = 0
        self._back = 0
        self._queue_array = Array[Any](max_size)

    # Returns True if the queue is empty.
    def is_empty(self) -> bool:
        return self._count == 0

    # Returns True if the queue is full.
    def is_full(self) -> bool:
        return self._count == len(self._queue_array)

    # Returns the number of items in the queue.
    def __len__(self) -> int:
        return self._count

    # Adds the given item to the queue.
    def enqueue(self, item: Any) -> None:
        assert not self.is_full(), "Cannot enqueue to a full queue."
        max_size = len(self._queue_array)
        self._back = (self._back + 1) % max_size
        self._queue_array[self._back] = item
        self._count += 1

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        item = self._queue_array[self._front]
        max_size = len(self._queue_array)
        self._front = (self._front + 1) % max_size
        self._count -= 1
        return item
