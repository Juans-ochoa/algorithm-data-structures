class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None

    def sorted_search(self, target):
        curr = self.__head

        while curr is not None and curr.data < target:
            curr = curr.next
            if curr.data == target:
                True

        return False

    # Insert nodes in sorted list
    def add(self, value):
        curr = self.__head
        prevNode = None

        while curr is not None and value > curr.data:
            prevNode = curr
            curr = curr.next

        node = Node(value)
        node.next = curr

        if curr is self.__head:
            self.__head = node
        else:
            prevNode.next = node

    # Traverse linked list

    def traverse(self):
        curr = self.__head

        while curr is not None:
            print(curr.data)
            curr = curr.next


test = LinkedList()
test.add(2)
test.add(3)
test.add(4)
test.add(1)
test.traverse()
