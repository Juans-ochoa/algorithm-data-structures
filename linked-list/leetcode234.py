class ListNode:
    def __init__(self, value: str | int) -> None:
        self.value = value
        self.next: "ListNode|None" = None


class Solution:
    def is_palindrome(self, head: "ListNode|None") -> bool:
        nums: list[int | str] = []

        while head:
            nums.append(head.value)
            head = head.next

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1

        return True

    def is_palindrome_optimized(self, head: "ListNode") -> bool:
        slow = head
        fast = head

        # Find the middle
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right and left:
            if left.value != right.value:
                return False
            left = left.next
            right = right.next

        return True


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(Solution().is_palindrome_optimized(head))
