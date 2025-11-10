from typing import Any


class _QNode:
    def __init__(self, value: Any):
        self.data = value
        self.next = None


class Queue:
    # Creates an empty queue.
    def __init__(self) -> None:
        self._q_head = None
        self._q_tail = None
        self._count = 0

    # Returns True f the queue is empty
    def is_empty(self) -> bool:
        return self._q_head == None

    # Returns the number of items in the queue.
    def __len__(self) -> int:
        return self._count

    # Adds the given item to the queue.
    def enqueue(self, item: Any):
        node = _QNode(item)

        if self.is_empty():
            self._q_head = node
        else:
            self._q_tail.next = node

        self._q_tail = node
        self._count += 1

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        node = self._q_head
        if self._q_head is self._q_tail:
            self._q_tail = None
        self._q_head = self._q_head.next
        self._count -= 1
        return node.data
