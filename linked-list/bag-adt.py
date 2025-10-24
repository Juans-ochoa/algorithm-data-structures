class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Bag:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def __contains__(self, item):
        currentNode = self.__head
        while currentNode is not None and currentNode.data != item:
            currentNode = currentNode.next

        return currentNode.data is not None

    def add(self, data):
        node = Node(data)
        node.next = self.__head
        self.__head = node
        self.__size += 1

    def remove(self, item):
        prev_node = None
        current = self.__head

        while current is not None and current.data != item:
            prev_node = current
            current = current.next

        assert current is not None, "The item must be in the bag."

        self.__size -= 1
        if current is self.__head:
            self.__head = current.next
        else:
            prev_node.next = current.next

            return current.data

    def __iter__(self):
        return _BagIterator(self.__head)

# Linked list iterators


class _BagIterator:
    def __init__(self, list_head):
        self._cur_node = list_head

    def __iter__(self):
        return self

    def next(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            data = self._cur_node.data
            self._cur_node = self._cur_node.next
            return data
