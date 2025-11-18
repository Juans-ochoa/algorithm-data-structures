class ListNode:
    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.next: "ListNode|None" = None


class Solution:
    def merge_tow_lists(self, l1: "ListNode|None", l2: "ListNode|None"):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
