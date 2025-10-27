class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def reorder_list(self, head: ListNode) -> None:
        # Find the middle
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next
        prev = slow.next = None
        while second is not None:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge two half
        first, second = head, prev
        while second is not None:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
