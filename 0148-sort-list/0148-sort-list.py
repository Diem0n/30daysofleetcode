# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        mid = self.find_middle(head)
        left = head
        right = mid.next
        mid.next = None

        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        return self.merge(left_sorted, right_sorted)

    def find_middle(self, head):
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return prev

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.val < right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next

        current = head

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        current.next = left if left else right

        return head     