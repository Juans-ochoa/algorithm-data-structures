class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# # Traverse a linked list


def traverse(head):
    current = head

    while current is not None:
        print(current.data, "\n")
        current = current.next


def addNode(head, value):
    new_node = Node(value)
    new_node.next = head

    return new_node


a = Node(1)
a = addNode(a, 2)
a = addNode(a, 3)
a = addNode(a, 4)


traverse(a)

# Searching for a node


def unorderedSearch(head, target):
    current = head

    while current is not None and current.data != target:
        current = current.next

    return current is not None


print(unorderedSearch(a, 5))

# Removing nodes


def removeNode(head, target):
    current = head
    prev_node = None

    while current is not None and current.data != target:
        prev_node = current
        current = current.next

    if current is not None:
        if current is head:
            head = current.next
        else:
            prev_node.next = current.next


print(removeNode(a, 3))
