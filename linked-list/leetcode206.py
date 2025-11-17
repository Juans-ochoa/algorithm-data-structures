class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: "ListNode|None" = None


class Solution:
    def reverse_list(self, head: "ListNode") -> ListNode | None:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reverse_recursive(self, head: "ListNode") -> ListNode | None:
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverse_recursive(head.next)
            head.next.next = head

        head.next = None

        return new_head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(Solution().reverse_recursive(head))
