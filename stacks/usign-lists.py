class Stack:
    # Create an empty stack
    def __init__(self):
        self._items = list()

    # Returns True is the stack is empty of False otherwise
    def is_empty(self):
        return len(self) == 0

    # Returns the number of items in the stack.
    def __len__(self):
        return len(self._items)

    # Returns the top item on the stack without removing it.
    def peek(self):
        return self._items[-1]

    # Removes and returns the top item on the stack
    def pop(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self._items.pop()

    # Push an item onto the top of the stack
    def push(self, item):
        self._items.append(item)
