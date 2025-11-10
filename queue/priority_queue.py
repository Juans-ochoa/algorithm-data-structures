from typing import Any
# Implementation of the unbounded priority Queue ADT using a Python list with new items appended to the end.


class PriorityQueue:
    # Creates an empty unbounded priority queue.
    def __init__(self) -> None:
        self._q_list: list["_PriorityQueue"] = list()

    # Returns True if the queue  is empty.
    def is_empty(self) -> bool:
        return len(self) == 0

    # Returns the number of items in the queue.
    def __len__(self) -> int:
        return len(self._q_list)

    def enqueue(self, item: Any, priority: int):
        # Create a new instance of the storage class append it to the list.
        entry = _PriorityQueue(item, priority)
        self._q_list.append(entry)

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        # Find the entry with the highest priority.
        highest = self._q_list[0].priority
        index: int = 0
        for i in range(self.__len__()):
            # See if the ith entry contains a higher priority (smaller integer).
            if self._q_list[i].priority < highest:
                index = i
                highest = self._q_list[i].priority
        # Removes the entry with the highest priority and return the item.
        entry = self._q_list.pop(index)
        return entry.item


class _PriorityQueue:
    def __init__(self, item: Any, priority: int) -> None:
        self.priority = priority
        self.item = item


queue = PriorityQueue()
queue.enqueue("purple", 5)
queue.enqueue("black", 1)
queue.enqueue("orange", 3)
queue.enqueue("white", 0)
queue.enqueue("green", 1)
queue.enqueue("yellow", 5)

while not queue.is_empty():
    item = queue.dequeue()
    print(item)
