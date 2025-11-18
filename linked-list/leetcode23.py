class ListNode:
    def __init__(self, value: int = 0):
        self.value = value
        self.next: "ListNode|None" = None


class Solution:
    def merge_k_lists(self, lists: list[ListNode | None]):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists: list[ListNode | None] = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.merge_list(l1, l2))

            lists = merged_lists

        return lists[0]

    def merge_list(self, l1: "ListNode|None", l2: "ListNode|None") -> "ListNode|None":
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

        if l2:
            tail.next = l2

        return dummy.next
