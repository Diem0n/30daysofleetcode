# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

    def split(head, step):
            i = 1
            while head and i < step:
                head = head.next
                i += 1
            if not head:
                return None
            next_head = head.next
            head.next = None
            return next_head

    def merge(left, right, head):
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
            while current.next:
                current = current.next
            return current  
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = self.get_length(head)

        dummy = ListNode(0)
        dummy.next = head
        step = 1
        while step < length:
            current = dummy.next
            tail = dummy
            while current:
                left = current
                right = Solution.split(left, step)
                current = Solution.split(right, step)
                tail = Solution.merge(left, right, tail)
            step *= 2

        return dummy.next

      