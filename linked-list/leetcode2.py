class ListNode:
    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.next: "ListNode|None" = None


class Solution:
    def add_two_numbers(self, l1: "ListNode|None", l2: "ListNode|None") -> ListNode | None:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 and l2 or carry:
            v1 = l1.value if l1 else 0
            v2 = l2.value if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # Update ptr
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(4)
l2.next = ListNode(5)
l2.next.next = ListNode(6)


Solution().add_two_numbers(l1, l2)
