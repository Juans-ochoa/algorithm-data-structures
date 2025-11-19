class ListNode:
    def __init__(self, value: int = 0, next: "ListNode|None" = None) -> None:
        self.value = value
        self.next = next


class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # Delete
        left.next = left.next.next

        return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

Solution().remove_nth_from_end(head, 6)
