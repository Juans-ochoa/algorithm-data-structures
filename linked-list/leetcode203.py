class ListNode:
    def __init__(self, value: int = 0, next: "ListNode|None" = None) -> None:
        self.value = value
        self.next = next


class Solution:
    def remove_elements(self, head: "ListNode", target: int) -> ListNode | None:
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            nxt = curr.next

            if curr.value == target:
                prev.next = nxt
            else:
                prev = curr

            curr = nxt
        return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

Solution().remove_elements(head, 3)
